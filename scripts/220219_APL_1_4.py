import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Chiss/Archive/Time-Lapse/220219_1_APL/*.tif',  # APL_099992 - APL_100107
    '/Volumes/Chiss/Archive/Time-Lapse/220219_4_APL/*.tif',  # APL_100698 - APL_101023
]
# poster: APL_100698


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 3, watermark=True, verbose=False, dryrun=False)
