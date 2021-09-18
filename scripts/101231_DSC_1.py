import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/101231_1/*.tiff'  # D80_101231_235618 - D80_110101_002307
# poster: D80_110101_000431


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 0, watermark=True, verbose=False, dryrun=False)
