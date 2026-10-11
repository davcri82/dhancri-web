"""Public files shared by the local preview and the link checker (stdlib only)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC_PAGES = ("index.html", "automation-trainer/index.html", "404.html")
PUBLIC_ROOT_FILES = ("robots.txt", "sitemap.xml")


def public_files():
    files = {ROOT / name for name in (*PUBLIC_PAGES, *PUBLIC_ROOT_FILES)}
    files.update(path for path in (ROOT / "assets").rglob("*") if path.is_file())
    return files
