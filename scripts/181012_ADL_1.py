import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/181012_1/*.tiff',  # ADL_243737 - ADL_244687
# poster: ADL_244569


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
