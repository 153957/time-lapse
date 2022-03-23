import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Chiss/Archive/Time-Lapse/220130_2_APL/*.tif'  # APL_098953 - APL_099267
# poster: APL_099267


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 2, watermark=True, verbose=False, dryrun=False)
