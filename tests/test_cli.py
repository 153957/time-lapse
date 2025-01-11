"""Tests for cli module."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import TestCase

from time_lapse import cli


class TestMakeMovie(TestCase):
    """Tests for the all-in-one function."""

    maxDiff = None

    def test_make_movie(self) -> None:
        """Check verbose output with dryrun."""
        with redirect_stdout(StringIO()) as stdout:
            cli.make_movie(
                name='1812',
                patterns='1812_*.tif',
                fps=48,
                deflicker=3,
                watermark=False,
                verbose=True,
                dryrun=True,
                filters=None,
            )

        output = stdout.getvalue()
        expected_output = (
            'ffmpeg -framerate 48 -pattern_type glob -i 1812_*.tif'
            ' -filter_complex [0]deflicker=mode=pm:size=3[s0]'
            ';[s0]concat=n=1[s1];[s1]scale=force_original_aspect_ratio=decrease:size=1920x1920[s2]'
            ';[s2]split=2[s3][s4];[s4]scale=force_original_aspect_ratio=decrease:size=960x960[s5]'
            ' -map [s3] -crf 20 -movflags faststart -pix_fmt yuv420p -preset slower 1812.mp4'
            ' -map [s5] -crf 20 -movflags faststart -pix_fmt yuv420p -preset slower 1812_960.mp4'
            '\n'
            'Install graphviz to generate a pdf of the signal graph'
            '\n'
        )
        self.assertEqual(expected_output, output)

        with self.subTest('Contains path to font when watermark is enabled'):
            with redirect_stdout(StringIO()) as stdout:
                cli.make_movie(
                    name='1812',
                    patterns='1812_*.tif',
                    fps=48,
                    deflicker=3,
                    watermark=True,
                    verbose=True,
                    dryrun=True,
                    filters=None,
                )

            output = stdout.getvalue()
            font_path = str(Path(__file__).parent.parent / 'time_lapse/fonts/Jost-400-Book.ttf')
            self.assertIn(font_path, output)
