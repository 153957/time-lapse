import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/121004_1/*.tiff'  # ARN_018617 - ARN_019151
# poster: ARN_018617


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 48, 5, watermark=True, verbose=False, dryrun=False)
