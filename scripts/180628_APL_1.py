import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/180628_1/*.tiff',  # APL_027178 - APL_027581
# poster: APL_027521


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 25, 0, watermark=True, verbose=False, dryrun=False)
