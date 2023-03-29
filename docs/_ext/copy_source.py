import shutil
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.config import Config


def copy(app: Sphinx, config: Config):
    copy_files = config.copy_files
    for src, dst in copy_files:
        srcdir = Path(".").resolve()
        if srcdir.is_dir():
            shutil.copytree(srcdir / src, srcdir / dst, dirs_exist_ok=True)
        else:
            shutil.copy(srcdir / src, srcdir / dst)


def setup(app: Sphinx):
    app.add_config_value("copy_files", [], "env")
    app.connect("config-inited", copy)
    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
