# Validación de v0.1

Comprobaciones realizadas localmente el 11 de octubre de 2026.

## Comprobación repetible

```sh
python3 scripts/validate.py
```

El validador usa solo la biblioteca estándar de Python. Comprueba:

- Enlaces internos, rutas de imágenes/CSS, anclas y enlaces entre plantillas.
- Metadatos básicos: idioma, viewport, title, descripción, canonical y Open Graph.
- Un `h1` y un `main` por página, IDs únicos y presencia de `alt` en imágenes.
- Existencia local de imágenes sociales y coherencia del sitemap.
- Exclusiones de Pages y ausencia de `.nojekyll` o rutas legales públicas en v0.1.
- Ausencia de elementos fuera de alcance: scripts, formularios e integraciones
  embebidas; revisión de recursos CSS/SVG y marcadores pendientes públicos.
- Enlaces internos de la documentación.

No es un validador completo de la especificación HTML ni una auditoría automática
de conformidad WCAG. No reemplaza la revisión visual y editorial.

## HTTP y navegador

Se sirvió el sitio con `python3 scripts/serve.py --port 8000` y se revisó en Chrome
headless mediante su protocolo de depuración, sin instalar dependencias en el proyecto.

| Comprobación | Resultado |
| --- | --- |
| Inicio, ficha de aplicación, 404 explícito, CSS e iconos | HTTP 200 |
| Rutas reservadas de privacidad ES/EN | HTTP 404 |
| Ruta anidada inexistente | HTTP 404 con la página de error del sitio |
| `_legal`, `docs`, `.git/config` | HTTP 404 |
| Inicio, ficha y error en anchos 320, 390, 768 y 1440 px | Sin desbordamiento horizontal en las 12 vistas |
| Imágenes y estilos en las 12 vistas | Cargados correctamente |
| SVG oficiales claro y oscuro en las 12 vistas | Cargados, proporción 1200:360 conservada, sin filtros CSS |
| Salto al contenido con Tab y Enter en las 12 vistas | Operativo |
| Scripts, formularios, peticiones fuera del origen local y errores de ejecución | Ninguno |

Se inspeccionaron capturas completas de escritorio y móvil de las páginas
principales, incluidas las cabeceras claras y los pies oscuros con los SVG oficiales.
Ambos SVG públicos se compararon byte a byte con sus originales del ZIP conservado
en `design/branding`; coinciden sin modificaciones. La navegación visible no requiere
menú JavaScript; en móvil ocupa
una fila bajo el logotipo. Los enlaces tienen foco visible, las imágenes decorativas
usan `alt` vacío y los gráficos explicativos tienen descripción.

## Límites y comprobaciones posteriores

Antes del commit de v0.1 se confirmó el remoto `davcri82/dhancri-web` y su rama
principal `main`, se revisaron los archivos candidatos y el contenido textual del
ZIP oficial sin detectar secretos ni datos personales. No hay archivos temporales
ni borradores de políticas entre los candidatos; `_legal` contiene documentación
del procedimiento y plantillas sin texto jurídico. El `.gitignore` excluye
credenciales locales, entornos Python y temporales sin ocultar recursos, originales
de diseño ni plantillas legítimas. El hash definitivo del commit se entrega junto
al resultado del push; puede consultarse con `git log -1 --format=%H`.

- No se ha desplegado el sitio ni ejecutado el tratamiento de Jekyll de GitHub.
  El validador comprueba la configuración, no un artefacto remoto. Antes de dar por
  terminado el primer despliegue autorizado, comprobar que `_legal`, `docs`, `design`
  y `scripts` no son accesibles y que las rutas legales siguen devolviendo 404.
- No se han probado dispositivos físicos, Safari, Firefox ni un lector de pantalla.
- No se han cambiado DNS ni comprobado certificado, redirecciones o indexación real.
- Las URLs SEO apuntan a `dhancri.com` como destino previsto; todavía no acreditan
  una publicación activa. La limitación del 404 bajo un prefijo temporal de proyecto
  se documenta en [DEPLOYMENT.md](DEPLOYMENT.md).
- Las plantillas legales solo están comprobadas estructuralmente. No son políticas
  jurídicas redactadas, completas o aprobadas; no se han publicado.
