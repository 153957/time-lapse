import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/190430_1_Waterfall/*.tiff',  # APL_050876 - APL_051061


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 2, watermark=True, verbose=False, dryrun=False)
