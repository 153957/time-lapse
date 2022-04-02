import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Jedi/Cache/220401_5_scholeksters/*.tif',  # APL_105173 - APL_105379
    '/Volumes/Jedi/Cache/220401_3_haarrijnseplas/*.tif',  # APL_104600 - APL_104697
    '/Volumes/Jedi/Cache/220401_4_haarrijnseplas/*.tif',  # APL_104727 - APL_105140
]
# poster: APL_105059


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 0, watermark=True, verbose=False, dryrun=False)
