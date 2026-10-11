# Recursos utilizados

Todos los archivos necesarios para el sitio público residen en `assets`. No se
requieren los repositorios de origen para servir o desplegar la web.

## DHANCRI Studio

Fuente incluida en el repositorio: `design/branding/DHANCRI_Studio_identidad_v0.1.zip`.
Los recursos se han extraído directamente de este ZIP, que se conserva intacto
y excluido del sitio público. Solo los archivos utilizados están en `assets/brand`.

| Archivo incorporado | Uso y transformación |
| --- | --- |
| `assets/brand/dhancri-studio_claro.svg` | SVG oficial intacto: cabeceras sobre fondo claro y favicon de portada |
| `assets/brand/dhancri-studio_oscuro.svg` | SVG oficial intacto: pies sobre fondo oscuro `#172634` |
| `assets/brand/dhancri-studio_oscuro.png` | Open Graph de la portada; original 1800 × 540 sin modificar |

El README del paquete identifica azul `#0872C4`, gris `#727B88`, fondo oscuro
`#172634` y Comfortaa Bold/Regular como referencia, convertida en trazados SVG.
La web no descarga Comfortaa: el logotipo no depende de fuentes instaladas.
El propietario confirma este paquete como identidad oficial aprobada. Ambos SVG
conservan sus dimensiones `1200 × 360`, `viewBox="0 0 1200 360"`, trazados y colores
originales. El tamaño en CSS se adapta con altura automática, sin recortar el lienzo,
deformar, aplicar filtros ni modificar la tipografía. La variante oscura conserva
el fondo `#172634`, las letras blancas y el gris `#CAD3DF` incluidos en el original.
Se ha eliminado la adaptación de lienzo compacto utilizada en la primera revisión.

## Automation Trainer

Fuente local:
`../automation_trainer/design/branding/Automation_Trainer_brand_v1/`.

| Archivo incorporado | Uso |
| --- | --- |
| `assets/brand/automation_trainer_blue.svg` | Icono en portada, tarjeta y ficha de aplicación; favicon de la ficha |
| `assets/brand/automation_trainer_blue_1024.png` | Open Graph de la ficha |

Ambos son originales intactos. La fuente describe el concepto aprobado como
engranaje blanco con birrete cian y fondo azul, con identidad independiente del estudio.
Sus colores son azul `#0072CE`, cian `#00AEEF`, gris oscuro `#1F2A37` y blanco.

## Ilustración y tipografía

`assets/illustrations/ladder.svg` es un esquema técnico vectorial creado para la web:
contacto normalmente abierto `I0.0` y bobina `Q0.0`. No es un logotipo, una captura
de pantalla ni una representación de la interfaz de Automation Trainer. Su carácter
conceptual se indica en la ficha.

La tipografía del contenido utiliza la pila del sistema; no hay archivos de fuentes,
CDN, imágenes remotas, librerías ni recursos de terceros. Las flechas son texto
decorativo oculto al lector de pantalla.

No se han utilizado ni copiado símbolos de Neón Automatismos o materialPRO.
