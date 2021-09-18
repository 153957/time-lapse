import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/151203/1/*.tiff',  # ADL_197037 - ADL_197259
    '/Volumes/Falcon/tl_temp/151203/3/*.tiff',  # ADL_197298 - ADL_197378 & ADL_197386 - ADL_197534
    '/Volumes/Falcon/tl_temp/151203/4/*.tiff',  # ADL_197555 - ADL_197678
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 0, watermark=True, verbose=False, dryrun=False)
