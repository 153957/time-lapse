import pathlib
import shutil

from PIL import Image


def create_thumbnail(
    name: str,
    poster_path: pathlib.Path,
    width: int = 180,
    height: int = 120,
) -> None:
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
