import pathlib
import shutil

from PIL import Image


def create_thumbnail(
    name: str,
    poster_path: pathlib.Path,
) -> None:
    target_path = pathlib.Path() / f'{name}.png'
    thumbnail_path = target_path.parent / f'{name}@2x.png'
    with Image.open(poster_path) as image:
        image.resize(
            size=(180, 120),
            resample=Image.LANCZOS,
        ).save(
            thumbnail_path,
            compress=False,
        )
    shutil.copy(poster_path, target_path)
