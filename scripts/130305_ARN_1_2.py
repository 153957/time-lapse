import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/130305_1/*.tiff',  # ARN_038167 - ARN_038476
    '/Volumes/Falcon/tl_temp/130305_2/*.tiff',  # ARN_038495 - ARN_039026
]
# poster: ARN_038262


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 48, 10, watermark=True, verbose=False, dryrun=False)
