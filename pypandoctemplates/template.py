from __future__ import annotations

import os
import shutil
from abc import ABC


formats = {
    "tex": "latex",
    "md": "markdown",
    "markdown": "markdown",
}


class PandocTemplate(ABC):
    """A base class for Pandoc templates"""

    #: Command line options for pandoc
    options: dict

    def __init__(self, **options):
        self.options = options or {}
        if "doc" not in self.options or not self.options["doc"]:
            raise ValueError("No document specified")
        if "to" not in self.options and self.options["doc"].split(".")[-1] not in formats:
            raise ValueError("The output format must be specified")
        self.setupTemplate()

    def setupTemplate(self):
        """Set up the template"""
        if "template" not in self.options:
            return
        template = self.options["template"].split(".")[0]
        fmt = self.options.get("to", formats[self.options["doc"].split(".")[-1]])

        templates = os.listdir(os.path.join(os.path.dirname(__file__), fmt))
        if template not in templates:
            raise ValueError(f"Template {template} not found in {fmt}")

        template_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), fmt, template))
        self.options["template"] = os.path.join(template_dir, f"{template}.{fmt}")
        for file in [
            os.path.join(template_dir, file) for file in os.listdir(template_dir) if file != f"{template}.{fmt}"
        ]:
            shutil.copy(file, os.getcwd())

    def render(self):
        """Render a template to a file"""
        options = " ".join(
            [
                f"{self.options['doc']}" if self.options["doc"] else "",
                f"--from {self.options['from']}" if self.options["from"] else "",
                f"--to {self.options['to']}" if self.options["to"] else "",
                f"--output {self.options['output']}" if self.options["output"] else "",
                f"--template {self.options['template']}" if self.options["template"] else "",
                f"--standalone" if self.options["standalone"] else "",
                f"--data-dir {self.options['data_dir']}" if self.options["data_dir"] else "",
                f"--defaults {self.options['defaults']}" if self.options["defaults"] else "",
            ]
        )
        os.system(f"pandoc {options}")
