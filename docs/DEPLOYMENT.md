# Publicación futura en GitHub Pages

**Documento de preparación del alojamiento.** La subida del código v0.1 a `main`
está autorizada. Activar Pages y configurar DNS siguen pendientes de autorización
independiente; no se han realizado esos cambios. Las políticas requieren además
su propia aprobación expresa.

## Activar desde la raíz

Una vez autorizada la publicación:

1. Ejecutar `python3 scripts/validate.py` y revisar la web localmente.
2. Confirmar que `_legal`, `docs`, `design`, `scripts` y `README.md` siguen excluidos en
   `_config.yml`, que no existe `.nojekyll` y que no hay archivos legales pendientes
   dentro de `privacy/`. La exclusión de Pages no oculta el código del repositorio.
3. Confirmar y subir los cambios aprobados a `main`.
4. En GitHub, abrir **Settings → Pages → Build and deployment**. Seleccionar
   **Deploy from a branch**, rama **main**, carpeta **/(root)** y guardar.
5. Esperar el resultado del despliegue nativo de Pages. Comprobar inicio, ficha,
   CSS, iconos y 404. Antes de aprobar privacidad, sus dos rutas deben devolver 404.

No se requiere npm, Flutter, framework, dependencias ni compilación local. No hay
workflow de despliegue propio. Pages utiliza su tratamiento nativo de Jekyll para
copiar estos archivos y aplicar exclusiones; los HTML no llevan front matter ni
plantillas. **No añadir `.nojekyll` ni desplegar toda la raíz como un artefacto
estático sin filtrar**: se serviría material interno. Si se migra a otro hosting,
publicar solo `index.html`, `404.html`, `automation-trainer/`, `assets/`, `robots.txt`
y `sitemap.xml` hasta aprobar más páginas.

Fuente: [configuración de la fuente de publicación](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
y [archivos que Jekyll excluye y configuración](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll).

## URL temporal de proyecto

Los enlaces de las dos páginas principales y sus recursos son relativos y funcionan
bajo el prefijo de un repositorio, como `/dhancri-web/`, además del dominio propio.
Los metadatos SEO y el sitemap apuntan al destino definitivo `https://dhancri.com`.

El `404.html` usa rutas desde la raíz para funcionar a cualquier profundidad de
`dhancri.com`. Si se publica primero exclusivamente bajo una URL de proyecto de
GitHub, anteponer `/dhancri-web` a sus rutas `/`, `/assets/css/site.css` y
`/assets/brand/dhancri-studio_claro.svg` y `/assets/brand/dhancri-studio_oscuro.svg`
mientras se prueba allí, y retirarlo al
conectar el dominio propio. Si se quiere indexar una URL temporal, ajustar también
canonical, Open Graph, robots y sitemap a esa URL real.

## DNS futuro de dhancri.com

No se ha creado `CNAME` porque aún no se ha activado el dominio. Confirmar antes la
cuenta u organización propietaria y usar su hostname real terminado en `.github.io`,
sin incluir el nombre del repositorio en el destino DNS.

Orden previsto, cuando exista autorización:

1. Verificar `dhancri.com` en la cuenta u organización de GitHub mediante el registro
   TXT exacto que proporcione GitHub. No se inventa aquí ese valor.
2. Configurar **Custom domain → dhancri.com** en Settings → Pages antes de apuntar
   el DNS. Al publicar desde rama, GitHub crea `CNAME` en la raíz de la rama;
   incorporar ese cambio al trabajo local antes de cambios posteriores.
3. Configurar el dominio raíz en el proveedor DNS. Los registros A indicados por
   GitHub, comprobados en su documentación el 11 de octubre de 2026, son:

   | Tipo | Nombre | Valor |
   | --- | --- | --- |
   | A | `@` | `185.199.108.153` |
   | A | `@` | `185.199.109.153` |
   | A | `@` | `185.199.110.153` |
   | A | `@` | `185.199.111.153` |

   Alternativa: ALIAS/ANAME al hostname real de Pages si lo admite el proveedor.
   Para IPv6, los AAAA opcionales actuales son `2606:50c0:8000::153`,
   `2606:50c0:8001::153`, `2606:50c0:8002::153` y `2606:50c0:8003::153`.
4. Si también se quiere `www.dhancri.com`, añadir un CNAME con nombre `www` al
   hostname de la cuenta u organización propietaria terminado en `.github.io`.
   No apuntarlo a una URL con protocolo o ruta. Mantener `dhancri.com` como dominio
   principal; Pages gestiona la redirección entre el apex y `www` configurados.
5. Revisar registros en conflicto antes de cambiarlos; preservar MX/TXT de otros
   servicios. No utilizar un comodín DNS para esta web.
6. Esperar la comprobación DNS y el certificado de Pages, activar **Enforce HTTPS**
   cuando esté disponible, y comprobar las URLs HTTPS, recursos y redirecciones.

Verificar de nuevo los valores en la [documentación oficial de dominio personalizado](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
antes de ejecutar cambios. Para el TXT, seguir [verificación del dominio](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages).

## Privacidad

La aprobación del diseño o de un despliegue corporativo no aprueba las políticas.
Seguir [_legal/README.md](../_legal/README.md) y publicar texto completo ES/EN solo
tras aprobación expresa. No basta con retirar `noindex` o desbloquear una ruta:
se requiere contenido legal final y revisión de las fuentes.
