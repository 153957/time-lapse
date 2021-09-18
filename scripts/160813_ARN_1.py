import os

from time_lapse import make_movie

NAME = os.path.basename(__file__).replace('.py', '')
PATTERN = '/Volumes/Falcon/tl_temp/160813_1_Rhein_am_Flammen/*.tiff',  # ARN_105144 - ARN_106213
# poster: ARN_105611


if __name__ == '__main__':
    make_movie(NAME, PATTERN, 60, 0, watermark=True, verbose=False, dryrun=False)
