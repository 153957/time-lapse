import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Chiss/Archive/Time-Lapse/201118_3_APL/*.tif',  # APL_077370 - APL_078182
# poster: APL_077399


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 0, watermark=True, verbose=False, dryrun=False)
