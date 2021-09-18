import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = '/Users/arne/Desktop/tl_autos/*.jpg',  # tbd


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 5, watermark=True, verbose=False, dryrun=False)
