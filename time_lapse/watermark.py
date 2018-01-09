import os

import ffmpeg

RENNER_FONT = os.path.join(os.path.dirname(__file__), 'fonts/Renner-Book.ttf')
FONT_OPTIONS = {
    'fontfile': RENNER_FONT,
    'fontcolor': 'white',
    'shadowcolor': 'black',
    'x': 'main_w-text_w-line_h',
}


def add_watermark(input, text='Arne de Laat', subtext='153957 Photography', fontsize=32):
    watermarked_input = (input
        .drawtext(text=text, fontsize=fontsize, y='main_h-3*line_h', **FONT_OPTIONS)
        .drawtext(text=subtext, fontsize=int(fontsize * 0.625), y='main_h-2*line_h', **FONT_OPTIONS)
    )
    return watermarked_input
