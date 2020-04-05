import os
import sys


def _rel_path(path):
    return os.path.join(
        getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__))), path
    )


from .bin import linux
from .bin import win32
from .windows_proxy import switch
from .controller import controller
from .gui import main
from .gui.main import start_gui
