import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Chiss/Falcon/Time-Lapse/WEN_1_Food/WEN_*.tif',  # WEN_052204 - WEN_052527
# poster: WEN_052257


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 2, watermark=True, verbose=False, dryrun=False)
