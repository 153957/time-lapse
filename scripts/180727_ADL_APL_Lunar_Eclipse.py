import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERNS = [
    '/Volumes/Falcon/tl_temp/180727_Moon/1_D700/*.tiff',  # ADL_240651 - ADL_240862
    '/Volumes/Falcon/tl_temp/180727_Moon/2_D700/*.tiff',  # ADL_240867 - ADL_241048
    '/Volumes/Falcon/tl_temp/180727_Moon/3_D500/*.tiff',  # APL_030936 - APL_031065
    '/Volumes/Falcon/tl_temp/180727_Moon/4_D500/*.tiff',  # APL_031073 - APL_031230
    '/Volumes/Falcon/tl_temp/180727_Moon/5_D700/*.tiff',  # ADL_241162 - ADL_241328
]


if __name__ == '__main__':
    make_movie(NAME, PATTERNS, 25, 10, watermark=True, verbose=False, dryrun=False)
