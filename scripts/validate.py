#!/usr/bin/env python3
"""Check public links, metadata, local assets and the v0.1 privacy publication guard."""

from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree

from site_common import PUBLIC_PAGES, ROOT, public_files


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids = set()
        self.refs = []
        self.meta = {}
        self.canonical = []
        self.h1_count = 0
        self.lang = None
        self.problems = []
        self.main_count = 0
        self.title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.problems.append(f"id duplicado: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1
        if tag == "title":
            self.title = True
        if tag == "img" and "alt" not in attrs:
            self.problems.append("imagen sin alt")
        if tag in {"script", "iframe", "form", "object", "embed"}:
            self.problems.append(f"elemento fuera del alcance v0.1: {tag}")
        for key in ("href", "src"):
            if key in attrs:
                self.refs.append((tag, key, attrs[key]))
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property", ""))] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))


def main():
    errors = []
    public = public_files()
    templates = set((ROOT / "_legal/templates").rglob("*.html"))
    pages = {}
    for path in sorted({ROOT / name for name in PUBLIC_PAGES} | templates):
        page = Page(path)
        page.feed(path.read_text())
        pages[path] = page
        if not page.lang or page.h1_count != 1 or page.main_count != 1 or not page.title:
            page.problems.append("revisar lang, title, h1 único y main único")
        if "viewport" not in page.meta:
            page.problems.append("falta viewport")
        errors.extend(f"{path.relative_to(ROOT)}: {error}" for error in page.problems)

    for path, page in pages.items():
        for tag, key, ref in page.refs:
            parts = urlsplit(ref)
            if parts.scheme or parts.netloc:
                if tag == "link" and ref in page.canonical:
                    continue
                errors.append(f"{path.relative_to(ROOT)}: dependencia/enlace externo no previsto: {ref}")
                continue
            target = ((ROOT if parts.path.startswith("/") else path.parent) / unquote(parts.path).lstrip("/")).resolve() if parts.path else path
            if target.is_dir():
                target = target / "index.html"
            allowed = public | templates if path in templates else public
            if target not in allowed or not target.is_file():
                errors.append(f"{path.relative_to(ROOT)}: enlace roto o no público: {ref}")
            if parts.fragment and (target not in pages or unquote(parts.fragment) not in pages[target].ids):
                errors.append(f"{path.relative_to(ROOT)}: ancla inexistente: {ref}")

    expected_urls = {"https://dhancri.com/", "https://dhancri.com/automation-trainer/"}
    for name in PUBLIC_PAGES[:2]:
        page = pages[ROOT / name]
        for key in ("description", "og:type", "og:title", "og:description", "og:url", "og:image", "og:image:alt"):
            if not page.meta.get(key):
                errors.append(f"{name}: falta metadato {key}")
        expected_url = "https://dhancri.com/" + name.removesuffix("index.html")
        if page.canonical != [expected_url] or page.meta.get("og:url") != expected_url:
            errors.append(f"{name}: canonical/og:url incorrecto")
        image_url = urlsplit(page.meta.get("og:image", ""))
        if image_url.netloc != "dhancri.com" or (ROOT / image_url.path.lstrip("/")) not in public:
            errors.append(f"{name}: imagen social inexistente o externa")

    sitemap = ElementTree.parse(ROOT / "sitemap.xml")
    urls = {node.text for node in sitemap.findall(".//{*}loc")}
    if urls != expected_urls:
        errors.append("sitemap: URLs inesperadas o incompletas")
    if "noindex" not in pages[ROOT / "404.html"].meta.get("robots", ""):
        errors.append("404: falta noindex")

    config = (ROOT / "_config.yml").read_text()
    exclusions = set(re.findall(r"^  - (.+)$", config, flags=re.MULTILINE))
    if not {"_legal", "docs", "design", "scripts", "README.md"} <= exclusions:
        errors.append("_config.yml: faltan exclusiones de publicación")
    if not re.search(r"^publish_drafts: false$", config, flags=re.MULTILINE):
        errors.append("_config.yml: publish_drafts debe permanecer false")
    if (ROOT / ".nojekyll").exists():
        errors.append(".nojekyll desactiva las exclusiones: retirar antes de publicar")
    if (ROOT / "privacy").exists():
        errors.append("La ruta pública privacy requiere texto final y aprobación expresa; actualizar el control solo tras aprobación")
    actual_html = {path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.html") if not any(part.startswith(("_", ".")) for part in path.relative_to(ROOT).parts)}
    if actual_html != set(PUBLIC_PAGES):
        errors.append(f"Páginas públicas no revisadas: {actual_html ^ set(PUBLIC_PAGES)}")
    for path in public:
        if not path.is_file():
            errors.append(f"Falta archivo: {path.relative_to(ROOT)}")
        if path.suffix in {".html", ".css", ".svg"}:
            source = path.read_text()
            if re.search(r"\[(?:NOMBRE|EMAIL|FECHA|.*PENDIENTE).*?\]", source, re.I):
                errors.append(f"Marcador pendiente en archivo público: {path.relative_to(ROOT)}")
            if path.suffix == ".css" and re.search(r"@import|url\s*\(", source, re.I):
                errors.append(f"Revisar dependencia CSS nueva: {path.relative_to(ROOT)}")
            if path.suffix == ".svg":
                svg = ElementTree.fromstring(source)
                for node in svg.iter():
                    if node.tag.rsplit("}", 1)[-1] in {"script", "foreignObject", "image"}:
                        errors.append(f"Contenido SVG no previsto: {path.relative_to(ROOT)}")

    for path in [ROOT / "README.md", *(ROOT / "docs").glob("*.md"), ROOT / "_legal/README.md"]:
        for ref in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            parts = urlsplit(ref)
            if not parts.scheme and not parts.netloc:
                target = (path.parent / unquote(parts.path)).resolve()
                if not target.is_file():
                    errors.append(f"{path.relative_to(ROOT)}: enlace de documentación roto: {ref}")

    if errors:
        print("VALIDACIÓN FALLIDA\n" + "\n".join(f"- {error}" for error in errors))
        raise SystemExit(1)
    print(f"OK: {len(PUBLIC_PAGES)} páginas públicas, {len(templates)} plantillas excluidas; enlaces, anclas, recursos, SEO y control de privacidad correctos.")


if __name__ == "__main__":
    main()
