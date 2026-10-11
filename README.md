# DHANCRI Studio — web corporativa v0.1

Web estática preparada para `https://dhancri.com` y publicación desde la raíz del
repositorio en GitHub Pages. HTML y CSS, sin JavaScript, paquetes, frameworks,
fuentes remotas ni compilación local. Todos los recursos están incluidos.

**Estado: v0.1 revisada y aprobada para subir el código a `davcri82/dhancri-web`,
rama `main`.** No se han activado GitHub Pages, configurado DNS ni añadido `CNAME`.
La subida del código no activa el alojamiento de la web. Las políticas de privacidad
permanecen fuera del árbol público, pendientes de texto final y aprobación expresa.

## Estructura

```text
index.html                           Presentación del estudio
automation-trainer/index.html        Presentación de Automation Trainer
404.html                             Página de error
assets/
  css/site.css                       Estilos compartidos y responsive
  brand/                             Identidades gráficas locales aprobadas
  illustrations/ladder.svg            Esquema conceptual, no captura de la app
sitemap.xml                          Dos páginas de contenido públicas
robots.txt                           Rastreo e indicación del sitemap
_config.yml                          Configuración nativa de Pages y exclusiones
design/branding/                     Paquete original de identidad, excluido del sitio
_legal/
  README.md                          Estado y procedimiento de aprobación
  templates/privacy/
    automation-trainer/index.html    Plantilla interna ES
    automation-trainer/en/index.html Plantilla interna EN
docs/
  ASSETS.md                          Procedencia de los recursos
  DEPLOYMENT.md                      Pages y configuración DNS futura
  VALIDATION.md                      Comprobaciones y límites
scripts/
  site_common.py                     Inventario de archivos públicos
  serve.py                           Previsualización pública con exclusiones
  validate.py                        Comprobación de enlaces y publicación legal
```

## Páginas

| Ruta | Estado |
| --- | --- |
| `/` | Implementada: estudio y primera aplicación |
| `/automation-trainer/` | Implementada: descripción educativa, Ladder y simulación |
| `/privacy/automation-trainer/` | Reservada; devuelve 404, sin política publicada |
| `/privacy/automation-trainer/en/` | Reservada; devuelve 404, sin política publicada |
| `/404.html` | Implementada; Pages la utilizará para direcciones inexistentes |

Las plantillas ES/EN están en `_legal`, excluida del sitio. Los borradores encontrados
en el proyecto Flutter tienen datos pendientes y no se han copiado al árbol público.
No se muestran enlaces de privacidad ni de Google Play antes de contar con sus
destinos aprobados/publicados. Tampoco se atribuyen certificaciones, valoraciones,
precios, fecha de lanzamiento ni funcionalidades no confirmadas.

## Uso local

Requiere únicamente Python 3.10 o posterior para estas herramientas opcionales:

```sh
python3 scripts/validate.py
python3 scripts/serve.py --port 8000
```

Abrir `http://127.0.0.1:8000/` y `http://127.0.0.1:8000/automation-trainer/`.
Detener con `Ctrl+C`. El servidor escucha solo en la interfaz local, no realiza
compilación y devuelve la página 404 con estado HTTP 404 para rutas inexistentes.
Bloquea `_legal`, documentación, scripts y metadatos Git. Evitar servir toda la raíz
con un servidor genérico si se desea comprobar el conjunto público real.

Las páginas principales también pueden abrirse como archivos HTML; el servidor es
preferible para comprobar rutas de directorio y errores 404. Las rutas del 404 se
resuelven desde la raíz, como en el futuro dominio personalizado.

## Diseño y mantenimiento

Se usan los recursos disponibles de DHANCRI Studio y Automation Trainer, sin
logotipos alternativos. Los SVG oficiales claro y oscuro de DHANCRI se extraen
del ZIP conservado en `design/branding`, sin modificar proporciones, lienzo, trazados
ni colores: se usan respectivamente en cabeceras y pies. La paleta principal es
azul `#0872C4`, gris `#727B88` en
el logotipo y fondo oscuro `#172634`; el icono conserva su propia paleta.
La composición técnica, los azules y los neutros mantienen afinidad con la dirección
visual de Neón Automatismos y materialPRO sin incorporar sus símbolos. La referencia
local consultada es la web de Neón Automatismos; no se ha localizado un manual de
materialPRO, por lo que no se afirma una validación formal frente a ese manual.
Ver [recursos y procedencia](docs/ASSETS.md).

- Editar los HTML directamente y mantener consistencia de navegación y pies.
- Cambiar colores, espaciados y responsive en `assets/css/site.css`.
- Mantener un único `h1`, jerarquía de encabezados, textos alternativos, salto al
  contenido, foco visible y navegación usable con teclado.
- Al añadir una página pública, actualizar `scripts/site_common.py`, sitemap,
  metadatos y enlaces. Las URLs canonical y Open Graph apuntan al dominio previsto;
  no implican que esté activo. Si cambia el dominio, actualizarlas también en
  `robots.txt`, `sitemap.xml` y `_config.yml`.
- Validar antes de publicar. No incorporar scripts externos, analítica, anuncios,
  cookies de seguimiento, formularios ni servicios de terceros. El sitio no utiliza
  almacenamiento del navegador.
- Para aprobar e incorporar privacidad, seguir [_legal/README.md](_legal/README.md).
  La actualización de la política dentro de Flutter corresponde a su repositorio.

## Publicación y pendientes

Las instrucciones completas están en [despliegue y DNS](docs/DEPLOYMENT.md).
GitHub Pages permite seleccionar una rama y su carpeta raíz como fuente. Se prepara
ese modo sin un workflow propio ni build de frontend; se conserva el tratamiento
nativo de Pages para excluir material interno. No añadir `.nojekyll`: desactivaría
las exclusiones. [Referencia oficial de GitHub](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Pendientes para una entrega pública:

- Activación de Pages con autorización independiente; diseño y subida del código
  v0.1 ya aprobados.
- Confirmación del titular GitHub para los registros DNS y configuración del dominio.
- Texto de privacidad ES/EN completo y aprobación expresa; detalles en `_legal`.
- Incorporación de enlace a Google Play solo cuando exista una ficha publicada.
- Capturas reales de Automation Trainer si se decide incorporarlas; no se han
  fabricado pantallas ni presentado el esquema Ladder como captura.

La web puede publicarse sin las políticas únicamente si se autoriza esa entrega;
no debe proporcionarse ninguna URL legal a la ficha de la app hasta que exista
contenido final aprobado y accesible. Ver [validación](docs/VALIDATION.md).
