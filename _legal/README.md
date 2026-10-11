# Privacidad — material excluido de GitHub Pages

Las rutas públicas reservadas son `/privacy/automation-trainer/` (ES) y
`/privacy/automation-trainer/en/` (EN). **No existen archivos públicos en esas
rutas en v0.1.** Devuelven 404 deliberadamente. Tampoco están en navegación,
Open Graph, sitemap ni enlaces alternativos públicos.

## Fuentes consultadas

Repositorio independiente `../automation_trainer`, leídas el 11 de octubre de 2026:

- `docs/release/PRIVACY_POLICY_ES.md`
- `docs/release/PRIVACY_POLICY_EN.md`
- `docs/release/PRIVACY_AUDIT.md`

Ambas políticas son borradores técnicos con marcadores pendientes y prohibición
expresa de publicar. No se han copiado ni convertido en políticas web. El informe
de auditoría es evidencia técnica, no una política definitiva. Los originales se
mantienen en el repositorio Flutter para no crear versiones divergentes.

Pendientes identificados en esas fuentes: identidad legal y datos del responsable,
contacto, fecha efectiva, versión release, URL definitiva, público objetivo y países
de distribución, revisión aplicable, comprobación del AAB final y las decisiones
técnicas pendientes indicadas por la auditoría.

## Plantillas

`templates/privacy/automation-trainer/index.html` y su variante `en/index.html`
contienen únicamente la estructura semántica, el idioma y el estilo para revisión
local. No contienen texto jurídico ni datos inventados. Sus rutas relativas
funcionan dentro de esta carpeta de revisión.

`_legal` queda excluida mediante `_config.yml` y por el prefijo `_` del tratamiento
normal de GitHub Pages. La previsualización pública local también la bloquea.
`noindex` es solo una ayuda para revisión, **no un control de publicación**.
Esta exclusión del sitio no oculta archivos del propio repositorio si este es público.

## Incorporación futura, exclusivamente tras aprobación expresa

1. Resolver los datos pendientes en las fuentes Flutter y obtener el texto final
   ES/EN y la aprobación expresa del propietario para publicarlo. Registrar la
   versión aprobada y su aprobación; verificar los extremos técnicos señalados
   en la auditoría con el release final.
2. Crear `privacy/automation-trainer/index.html` y
   `privacy/automation-trainer/en/index.html` a partir de las plantillas. Incorporar
   el texto completo aprobado, con fecha efectiva e identidad/contacto reales.
3. Eliminar el aviso interno, el código de ruta reservada y los comentarios de
   revisión. Ajustar títulos, descripciones, canonical, Open Graph y `lang`.
   Cambiar CSS y logo a `../../assets/…` (ES) y `../../../assets/…` (EN), y el
   enlace de inicio a `../../` y `../../../`, respectivamente.
4. Añadir enlaces alternativos `hreflang="es"`, `hreflang="en"` y el selector de
   idioma recíproco. Añadir enlaces de privacidad desde la ficha y el pie de la web,
   y ambas URLs al sitemap. Mantener el texto ES/EN equivalente.
5. Actualizar la lista de páginas públicas de `scripts/site_common.py` y el control
   de privacidad de `scripts/validate.py`, solamente en el cambio aprobado. Ejecutar
   validación, revisar localmente y solicitar autorización para publicar si aún
   no existe. No retirar la exclusión de `_legal`.

No trasladar el borrador con marcadores al árbol público, ni activar rutas vacías
o avisos provisionales con apariencia de política definitiva.
