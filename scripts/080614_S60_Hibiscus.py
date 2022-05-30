import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Crimson/Cache/080614_S60_Hibiscus/*.tif',  # S60_080614_015644 - S60_080614_120341
# poster: S60_080614_075141


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 24, 5, watermark=True, verbose=False, dryrun=False)
