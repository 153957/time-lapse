import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Crimson/Cache/150205_ARN_1/*.tif',  # ARN_085754 - ARN_085843
    '/Volumes/Crimson/Cache/150206_ARN_1/*.tif',  # ARN_086517 - ARN_086960
]
# poster: ARN_085843


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
