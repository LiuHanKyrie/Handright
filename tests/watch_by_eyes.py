# coding: utf-8
""" Doing the tests with your naked eyes """
import pathlib

from PIL import Image as image

from tests.util import *
from pylf import *

SEED = "PyLf"


def test_handwrite2():
    template2 = {"backgrounds": (image.open(get_path("data/backgrounds/even-odd-letter/村庄信笺纸.jpg")),
                                 image.open(get_path("data/backgrounds/even-odd-letter/树信笺纸.jpg"))),
                 "margins": ({"left": 20, "top": 100, "right": 15, "bottom": 280},
                             {"left": 20, "top": 100, "right": 15, "bottom": 490}),
                 "line_spacings": (44, 44),
                 "font_sizes": (37, 37),
                 "font": get_default_font()}
    for file in pathlib.Path(get_path("data/texts")).iterdir():
        print(file)
        with file.open(encoding='utf-8') as f:
            text = f.read()
        images = handwrite2(text, template2, seed=SEED)
        for im in images:
            im.show()
        assert input("Like it? [Y/N] ").upper() == 'Y'


if __name__ == '__main__':
    print("""Test by naked eyes:""")
    print("""======================================
    Test: pylf.handwrite2""")
    test_handwrite2()
