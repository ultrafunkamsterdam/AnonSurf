import os
import sys


def rel_path(rel_path):
    return os.path.join(
        getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))), rel_path
    )

from .gui import start_gui


