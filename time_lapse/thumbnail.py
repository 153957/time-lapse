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
        image.resize(
            size=(width, height),
            resample=Image.LANCZOS,
        ).save(
            thumbnail_path,
            compress=False,
        )
    shutil.copy(poster_path, target_path)
