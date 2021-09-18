import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = '/Volumes/Falcon/tl_temp/110209_1/*.tiff',  # D700_110209_081219 - D700_110209_081737
# poster: D700_110209_081233


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 25, 0, watermark=True, verbose=False, dryrun=False)
