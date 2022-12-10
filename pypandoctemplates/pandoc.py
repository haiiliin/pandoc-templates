import os
import shutil


formats = {
    "tex": "latex",
    "md": "markdown",
    "markdown": "markdown",
}


def pandoc(
    doc,
    *,
    to=None,
    output=None,
    template=None,
    **kwargs,
):
    """Convert a markdown file to another format using Pandoc

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
        fmt = to or output.split(".")[-1]
        templates = os.listdir(os.path.join(os.path.dirname(__file__), formats[fmt]))
        if template not in templates:
            raise ValueError(f"Template {template} not found in {fmt}")

        template_dir: str = os.path.abspath(os.path.join(os.path.dirname(__file__), formats[fmt], template))
        template = os.path.join(template_dir, f"{template}.{formats[fmt]}")
        for file in [
            os.path.join(template_dir, file) for file in os.listdir(template_dir) if file != f"{template}.{formats[fmt]}"
        ]:
            shutil.copy(file, os.getcwd())
    options = [
        f"{doc}" if doc else "",
        f"--to={to}" if to else "",
        f"--output {output}" if output else "",
        f"--template {template}" if template else "",
    ] + [f"--{key}={value}" for key, value in kwargs.items()]
    options = " ".join(options)
    print(f"Evaluating: pandoc {options}")
    os.system(f"pandoc {options}")