from __future__ import annotations

import os
import shutil
from abc import ABC
from typing import Type


class MarkdownToAnythingTemplate(ABC):
    """A base class for Pandoc templates"""

    #: the pandoc template name
    format: str = None
    #: the file suffix for the output file
    suffix: str = None

    #: the template file name
    template_filepath: str = None
    #: suffixes to copy
    suffixes = []

    def __init__(self, template: str):
        self.setupTemplate(template)

    def setupTemplate(self, template: str):
        """Set up the template"""
        template = template.split(".")[0]
        templates = os.listdir(os.path.join(os.path.dirname(__file__), self.format))
        if template not in templates:
            raise ValueError(f"Template {template} not found in {self.format}")

        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), self.format, template))
        self.template_filepath = os.path.join(template_dir, f"{template}.{self.format}")
        for f in [
            os.path.join(template_dir, f)
            for f in os.listdir(template_dir)
            if f != f"{template}.{self.format}" and f.split(".")[-1] in self.suffixes
        ]:
            shutil.copy(f, os.getcwd())

    def render(self, doc: str, output: str, options: str = None):
        """Render a template to a file

        Args:
            doc: the path to the document
            output: the path to the output file
            options: extra options passed to pandoc
        """
        output = output or f"{doc.split('.')[0]}.{self.suffix}"
        options = options or ""
        cmd = (
            f"pandoc --from markdown --to {self.format} --template {self.template_filepath} "
            f"--output {output} {options} {doc}"
        )
        message = f"Running the following abaqus command: "
        length = max(len(message), len(cmd) + 4)
        print("-" * length, message, f"    {cmd}", "-" * length, sep="\n")
        os.system(cmd)


class MarkdownToLaTeXTemplate(MarkdownToAnythingTemplate):
    """A LaTeX template for Pandoc"""

    format = "latex"
    suffix = "tex"
    suffixes = ["bst", "cls", "sty", "tex"]


def TemplateClass(f: str) -> Type[MarkdownToAnythingTemplate]:
    """Get a template for a given format

    Args:
        f: the format to get a template for
    """
    Templates = {"latex": MarkdownToLaTeXTemplate}
    return Templates[f]
