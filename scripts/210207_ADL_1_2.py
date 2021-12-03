import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/210207_ADL_1/*.tif',  # ADL_276254
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/210207_ADL_2/*.tif',  # ADL_277263
]
# poster: ADL_276254


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 60, 4, watermark=True, verbose=False, dryrun=False)
