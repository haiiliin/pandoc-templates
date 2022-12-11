from __future__ import annotations

import os
import shutil
from typing import Dict, List, NamedTuple
from typing_extensions import Self


class TemplateFormat(NamedTuple):
    #: The name of the template format
    name: str = None
    #: The extensions of the template format
    exts: List[str] = None
    #: The required file extensions for the template format
    required_exts: List[str] = None


formats: Dict[str, TemplateFormat] = {}


def register(cls):
    """A decorator to register a format"""
    formats[cls.name] = cls()
    return cls


@register
class LaTeX(TemplateFormat):
    name = "latex"
    exts = ["tex"]
    required_exts = ["bib", "bst", "cls", "latex", "md", "sty", "tex"]


@register
class Markdown(TemplateFormat):
    name = "markdown"
    exts = ["md", "markdown"]
    required_exts = ["md", "markdown"]


class Template(NamedTuple):
    #: The format of the template
    fmt: TemplateFormat
    #: The name of the template
    name: str
    #: The path to the template
    filepath: str

    def copy_resources(self, dest: str = '.') -> Self:
        """Copy the resources of the template to the destination directory.

        Args:
            dest: The destination directory
        """
        filedir = os.path.dirname(self.filepath)
        for file in os.listdir(filedir):
            filepath = os.path.join(filedir, file)
            ext = os.path.splitext(file)[1][1:]
            if os.path.isfile(filepath) and ext in self.fmt.required_exts:
                shutil.copy(filepath, dest)
                print(f"Copying {file} to {dest}")
        return self


class TemplateDict(Dict):
    """A dictionary of templates, the fmt attribute must be existed"""

    def get(self, fmt_or_ext: str):
        templates = [template for fmt, template in self.items() if fmt_or_ext in template.fmt.exts or fmt_or_ext == fmt]
        if len(templates) == 0:
            raise ValueError(f"Unsupported format: {fmt_or_ext}")
        elif len(templates) > 1:
            raise ValueError(f"Ambiguous format: {fmt_or_ext}")
        return templates[0]

    def __getitem__(self, item):
        return self.get(item)


class TemplateFactory(TemplateDict[str, Template]):
    #: The format of the templates
    fmt: TemplateFormat
    #: The directory where the templates are stored
    basedir: str

    def __init__(self, fmt: TemplateFormat, basedir: str):
        super().__init__()
        self.fmt = fmt
        self.basedir = basedir
        self.setup()

    def setup(self, filedir: str = None):
        filedir = filedir or self.basedir
        for file_or_dir in os.listdir(filedir):
            path = os.path.join(filedir, file_or_dir)
            if os.path.isdir(path):
                self.setup(path)
            else:
                ext = os.path.splitext(file_or_dir)[1][1:]
                if ext == self.fmt.name:
                    name = os.path.splitext(file_or_dir)[0]
                    self[name] = Template(self.fmt, name, path)

    def get(self, fmt_or_ext: str) -> Template:
        return super().get(fmt_or_ext)


template_basedir = os.path.dirname(__file__)


class TemplateManager(TemplateDict[str, TemplateFactory]):

    def __init__(self, relative_to=template_basedir, **filedirs: str):
        super().__init__()
        for fmt, filedir in filedirs.items():
            filedir = os.path.join(relative_to, filedir)
            self[fmt] = TemplateFactory(formats[fmt], filedir)

    def get(self, fmt_or_ext: str) -> TemplateFactory:
        return super().get(fmt_or_ext)


manager = TemplateManager(latex="latex")


def pandoc(
    *doc,
    to=None,
    output=None,
    template=None,
    **kwargs,
):
    """Convert a markdown file to another format using Pandoc

    >>> pandoc("test.md", to="latex", output="test.tex", template="ascelike-new")
    Copying ... to ...
    ...
    Evaluating: pandoc test.md --to=latex --output test.tex --template ...ascelike-new.latex

    Args:
        doc (str): The markdown file to convert.
        to (str): The format to convert to.
        output (str, optional): Write output to FILE instead of stdout. Defaults to None.
        template (str, optional): Use a custom template. Defaults to None.
        **kwargs: Additional arguments to pass to pandoc.
    """
    if not doc:
        raise ValueError("No document specified")
    if not to and len(output.split(".")) < 2:
        raise ValueError("The output format must be specified")
    if template:
        fmt_or_ext = to or output.split(".")[-1]
        try:
            template = manager.get(fmt_or_ext).get(template).copy_resources().filepath
        except (ValueError, KeyError):
            pass
    docs = " ".join(doc)
    options = [
        f"{docs}" if docs else "",
        f"--to={to}" if to else "",
        f"--output {output}" if output else "",
        f"--template {template}" if template else "",
    ] + [f"--{key}={value}" for key, value in kwargs.items()]
    options = " ".join(options)
    cmd = f"pandoc {options}"
    print(f"Evaluating: {cmd}")
    os.system(cmd)
