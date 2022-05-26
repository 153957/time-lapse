import os

from time_lapse import make_movie, output, source

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Jedi/Cache/220517_APL_1/*.tif'  # APL_112805 - APL_113025
# poster: APL_112805


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 2, watermark=True, verbose=False, dryrun=False)
