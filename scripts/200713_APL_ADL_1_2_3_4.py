import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_ADL_1/*.tif',  # ADL_270285 - ADL_270486
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_APL_1/*.tif',  # APL_071330 - APL_071792
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_ADL_3/*.tif',  # ADL_270666 - ADL_270994
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_APL_2/*.tif',  # APL_071813 - APL_072132
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_ADL_4/*.tif',  # ADL_270995 - ADL_271219
    '/Volumes/Sith/Store_elsewhere/Falcon/Time-Lapse/200712_APL_3/*.tif',  # APL_072333 - APL_072917
]
# poster: APL_071934

if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 30, 5, watermark=True, verbose=False, dryrun=False)
