import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/180921_1/*.tiff',  # APL_037696 - APL_038030
# poster: APL_037883


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 3, watermark=True, verbose=False, dryrun=False)
