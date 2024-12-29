"""Function related to creating thumbnails."""
import pathlib
import shutil

from PIL import Image


def create_thumbnail(
    name: str,
    poster_path: pathlib.Path,
    width: int = 180,
    height: int = 120,
) -> None:
    """Create a thumbnail of the desired size for a given source image.

    The image will be cropped if the target aspect ratio does not
    match the aspect ratio of the source image.

    :param name: Name of the output thumbnail file.
    :param poster_path: Path to the source image.
    :param width: Target pixel width of the thumbnail.
    :param height: Target pixel height of the thumbnail.

    """
    target_path = pathlib.Path() / f'{name}{poster_path.suffix}'
    thumbnail_path = target_path.parent / f'{name}@2x.png'

    with Image.open(poster_path) as image:
        desired_ratio = width / height
        current_ratio = image.width / image.height

        box = None
        if desired_ratio > current_ratio:
            # Original to high
            box = (0, 0, image.width, image.width // desired_ratio)
        elif desired_ratio < current_ratio:
            # Original to wide
            box = (0, 0, image.height // desired_ratio, image.height)

        image.crop(
            box=box,
        ).resize(
            size=(width, height),
            resample=Image.Resampling.LANCZOS,
        ).save(
            thumbnail_path,
            compress=False,
        )
    shutil.copy(poster_path, target_path)
