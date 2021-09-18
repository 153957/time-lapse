import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/190430_2_Waterfall/*.tiff',  # APL_051279 - APL_051377
    '/Volumes/Falcon/tl_temp/190430_3_Waterfall/*.tiff',  # APL_051518 - APL_051747
    '/Volumes/Falcon/tl_temp/190430_4_Waterfall/*.tiff',  # APL_051753 - APL_051862
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 0, watermark=True, verbose=False, dryrun=False)
