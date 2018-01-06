import os

import ffmpeg

RENNER_FONT = os.path.join(os.path.dirname(__file__), 'fonts/Renner-Book.ttf')
FONT_OPTIONS = {
    'fontfile': RENNER_FONT,
    'fontcolor': 'white',
    'shadowcolor': 'black'
}


def add_watermark(input):
    watermarked_input = (input
        .filter_(
            'drawtext', text='Arne de Laat', fontsize=20, **FONT_OPTIONS
        )
        .filter_(
            'drawtext', text='153957 Photography', fontsize=16, **FONT_OPTIONS
        )
    )
    return watermarked_input
