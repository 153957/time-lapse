Time-Lapse assembling
=====================

[![PyPI](https://img.shields.io/pypi/v/time-lapse)](https://pypi.org/project/time-lapse/)
[![License](https://img.shields.io/github/license/153957/time-lapse)](https://github.com/153957/time-lapse/blob/master/LICENSE)
[![Build](https://img.shields.io/github/workflow/status/153957/time-lapse/Run%20tests)](https://github.com/153957/time-lapse/actions)

This repo contains tools used to compile Time-lapse movies using
ffmpeg. The ffmpeg utility is controlled via the ffmpeg-python wrapper.

Example usage of this package can be found in the
[time-lapse scripts](https://github.com/153957/time-lapse-scripts) repository.

Installation
============

This package requires the `ffmpeg` tool to be installed.

    brew install ffmpeg

Then install this package:

    pip install time-lapse

Additionally, when using the verbose output option a graph will be
rendered using `graphviz`, this requires the Graphviz library and the
related Python package:

    brew install graphviz
    pip install time-lapse[graph]

Codec
=====

For near-universal compatibility the H.264 codec is used. The following
section describe some of the choices for specific configuration options.

See the ffmpeg wiki for additional information:
<https://trac.ffmpeg.org/wiki/Encode/H.264>

Constant Rate Factor
--------------------

This uses `-crf 20` to set a constant rate factor, which means the overall
quality of the movie should be constant. So bitrate varies to ensure
this. Higher value is lower quality. The quality and bit rates at this
value seem reasonable.

Preset
------

`-preset slower` is used to improve the compression ratio for the selected
quality (crf), without taking too much time.

Faststart
---------

`-movflags +faststart` is used to allow the movie to quickly start playing,
while it is still loading or buffering.

Quicktime support
-----------------

The codec defaults to YUV 444, which is not supported by Quicktime. So
add `pix_fmt yuv420p` to fix Quicktime support.

Input
=====

Select input frames
-------------------

Use frames as input by giving a glob pattern which matches the desired
images. Usually these will be tiff images so use
`-pattern_type glob -i "*.tiff"`.

Framerate
---------

When using image sequences as input the framerate of the desired output
should be given using `-framerate 30`.

Filters
=======

Commonly used filters:

-   Deflicker <https://ffmpeg.org/ffmpeg-filters.html#toc-deflicker>
-   Scale <https://ffmpeg.org/ffmpeg-filters.html#scale>
-   Crop <https://ffmpeg.org/ffmpeg-filters.html#crop>
-   Drawtext <https://ffmpeg.org/ffmpeg-filters.html#drawtext-1>
-   Video sizes <https://ffmpeg.org/ffmpeg-utils.html#video-size-syntax>

Steps
-----

-   First deflicker the video to ensure it is equally deflickered for
    all outputs
-   Then scale and crop the videos to fit the desired final resolutions
-   Then add the watermark (which should not be deflickered)

Scale video
-----------

Add scaling to ensure it fits in given dimensions. Negative values for
width or height make the encoder figure out the size by itself, keeping
the aspect ratio of the source. The integer of the negative value, i.e.
4 for -4, means that the size should be devisble by that value. TODO:
does it just scale/squish the video or crop?:

    -vf scale=1920:-2
    -vf scale=960:540:aspect..

Convert movie
=============

Using time-lapse to find tif files, and create a movie called 'test_movie'
with 24 fps and deflickered:

    from time_lapse import output, source

    source_input = source.get_input(['*.tif'], fps=24, deflicker=10)
    output.create_outputs(source_input, 'test_movie', verbose=False)

Inspection
----------

By passing `verbose=True` to create outputs the following ffmpeg-python
inspection methods will be performed.

Show the ffmpeg command options ffmpeg-python would use:

    .get_args()

By using graphviz the graph from input to output can be shown using:

    .view()
