# Time-Lapse assembling

[![PyPI](https://img.shields.io/pypi/v/time-lapse)](https://pypi.org/project/time-lapse/)
[![License](https://img.shields.io/github/license/153957/time-lapse)](https://github.com/153957/time-lapse/blob/main/LICENSE)
[![Build](https://img.shields.io/github/actions/workflow/status/153957/time-lapse/tests.yml?branch=main)](https://github.com/153957/time-lapse/actions)

Este repositorio contiene herramientas utilizadas para compilar películas de Time-lapse usando
ffmpeg. La utilidad ffmpeg se controla a través del wrapper ffmpeg-python.

Se puede encontrar un ejemplo de uso de este paquete en el
repositorio de [time-lapse scripts](https://github.com/153957/time-lapse-scripts).

## Convertir película

Usando time-lapse para buscar archivos tif y crear una película llamada 'test_movie'
con 24 fps y deflickered:

    from time_lapse import output, source

    source_input = source.get_input(['*.tif'], fps=24, deflicker=7, filters=None)
    output.create_outputs(source_input, 'test_movie', verbose=False)

Esto también se puede hacer a través de la CLI:

    timelapse --name test_movie --pattern "*.tif" --fps 24 --deflicker 7

### Inspección

Al pasar `verbose=True` a create outputs, se realizarán los siguientes métodos de
inspección de ffmpeg-python.

Mostrar las opciones del comando ffmpeg que usaría ffmpeg-python:

    .get_args()

Usando graphviz, el grafo desde la entrada hasta la salida se puede mostrar mediante:

    .view()

## Instalación

Este paquete requiere que la herramienta `ffmpeg` esté instalada.

    brew install ffmpeg-full

Luego instale este paquete:

    pip install time-lapse

Adicionalmente, al usar la opción de salida verbose, se renderizará un grafo usando
`graphviz`, lo cual requiere la librería Graphviz y el paquete de Python relacionado:

    brew install graphviz
    pip install time-lapse[graph]

## Codec

Para una compatibilidad casi universal se utiliza el codec H.264. La siguiente
sección describe algunas de las elecciones para opciones de configuración específicas.

Consulte la wiki de ffmpeg para obtener información adicional:
<https://trac.ffmpeg.org/wiki/Encode/H.264>

### Factor de Tasa Constante (Constant Rate Factor)

Esto utiliza `-crf 20` para establecer un factor de tasa constante, lo que significa que la
calidad general de la película debe ser constante. Por lo tanto, la tasa de bits varía
para asegurar esto. Un valor más alto significa menor calidad. La calidad y las tasas de bits
en este valor parecen razonables.

### Preset

Se utiliza `-preset slower` para mejorar la tasa de compresión para la calidad seleccionada
(crf), sin tomar demasiado tiempo.

### Faststart

Se utiliza `-movflags +faststart` para permitir que la película comience a reproducirse
rápidamente, mientras aún se está cargando o almacenando en búfer.

### Soporte de Quicktime

El codec utiliza por defecto YUV 444, que no es soportado por Quicktime. Por lo tanto,
agregue `pix_fmt yuv420p` para solucionar el soporte de Quicktime.

## Entrada

### Seleccionar fotogramas de entrada

Use fotogramas como entrada proporcionando un patrón glob que coincida con las imágenes
deseadas. Generalmente estas serán imágenes tiff, así que use
`-pattern_type glob -i "*.tiff"`.

### Tasa de fotogramas (Framerate)

Al usar secuencias de imágenes como entrada, se debe indicar la tasa de fotogramas del
resultado deseado usando `-framerate 30`.

## Filtros

Filtros comúnmente utilizados:

- Deflicker <https://ffmpeg.org/ffmpeg-filters.html#toc-deflicker>
- Scale <https://ffmpeg.org/ffmpeg-filters.html#scale>
- Crop <https://ffmpeg.org/ffmpeg-filters.html#crop>
- Drawtext <https://ffmpeg.org/ffmpeg-filters.html#drawtext-1>
- Tamaños de video <https://ffmpeg.org/ffmpeg-utils.html#video-size-syntax>

### Pasos

El orden óptimo para aplicar deflicker/scale/watermarking es el siguiente:

- Primero deflicker el video para asegurar que esté igualmente deflickered para
  todas las salidas.
- Luego escale y recorte (crop) los videos para que se ajusten a las resoluciones finales deseadas.
- Luego agregue la marca de agua (la cual no debe ser deflickered y debe tener un tamaño constante).

### Escalar video

Agregue escalado para asegurar que encaje en las dimensiones dadas. Los valores negativos para
el ancho o el alto hacen que el codificador determine el tamaño por sí mismo, manteniendo
la relación de aspecto de la fuente. El entero del valor negativo, por ejemplo 4 para -4,
significa que el tamaño debe ser divisible por ese valor. TODO:
¿simplemente escala/estira el video o lo recorta?:

    -vf scale=1920:-2
    -vf scale=960:540:aspect..
