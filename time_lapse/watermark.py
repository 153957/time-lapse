import pathlib

import ffmpeg

JOST_FONT = pathlib.Path(__file__).parent / 'fonts/Jost-400-Book.ttf'
FONT_OPTIONS = {
    'fontfile': JOST_FONT,
    'fontcolor': 'white',
    'shadowcolor': 'black',
    'x': 'main_w - text_w - text_h',
    'y_align': 'baseline',
}


def add_watermark(
    input_node: ffmpeg.nodes.FilterNode,
    text: str,
    subtext: str,
    fontsize: int = 32,
) -> ffmpeg.nodes.FilterNode:
    watermarked_input = input_node.drawtext(
        text=text,
        fontsize=fontsize,
        y='main_h - (text_h * 2)',
        **FONT_OPTIONS,
    ).drawtext(
        text=subtext,
        fontsize=int(fontsize * 0.625),
        y='main_h - text_h',
        **FONT_OPTIONS,
    )
    return watermarked_input
