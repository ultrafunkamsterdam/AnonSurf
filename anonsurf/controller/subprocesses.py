import os
import subprocess


def subprocess_args(include_stdout=True):
    if hasattr(subprocess, "STARTUPINFO"):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        env = os.environ
    else:
        si = None
        env = None
    if include_stdout:
        ret = {"stdout": subprocess.PIPE}
    else:
        ret = {}
    ret.update(
        {
            "stdin": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "startupinfo": si,
            "env": env,
        }
    )
    return ret
