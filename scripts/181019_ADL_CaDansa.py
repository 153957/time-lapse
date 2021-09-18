import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/181021_1/*.tiff',  # ADL_248271 - ADL_249074
    '/Volumes/Falcon/tl_temp/181019_2/*.tiff',  # ADL_246049 - ADL_247034
    '/Volumes/Falcon/tl_temp/181021_2/*.tiff',  # ADL_249084 - ADL_249805
    '/Volumes/Falcon/tl_temp/181020_1/*.tiff',  # ADL_247427 - ADL_248067
    '/Volumes/Falcon/tl_temp/181019_3/*.tiff',  # ADL_247060 - ADL_247415
    '/Volumes/Falcon/tl_temp/181020_2/*.tiff',  # ADL_248070 - ADL_248261
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 24, 3, watermark=True, verbose=False, dryrun=False)
