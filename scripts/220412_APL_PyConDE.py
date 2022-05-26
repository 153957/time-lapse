import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Jedi/Cache/220412_APL_1/*.tif',  # APL_106405 - APL_106895
    '/Volumes/Jedi/Cache/220412_APL_2/*.tif'  # APL_106899 - APL_107507
]
# poster: APL_106899


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 0, watermark=True, verbose=False, dryrun=False)
