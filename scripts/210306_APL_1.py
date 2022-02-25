import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Chiss/Temporary/210306_APL_1/APL_*.tif',  # APL_081153 - APL_081520
# poster: APL_081301


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 2, watermark=True, verbose=False, dryrun=False)
