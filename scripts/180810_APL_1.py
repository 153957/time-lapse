import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/180810_APL_1/*.tif',  # APL_033321 - APL_033801
# poster: APL_033611


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 30, 2, watermark=True, verbose=False, dryrun=False)
