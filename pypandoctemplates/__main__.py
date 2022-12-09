import argparse

from .templates import TemplateClass


def cli():
    parser = argparse.ArgumentParser(prog="pypandoctemplates", description="pypandoctemplates command line interface")
    parser.add_argument("doc", metavar="doc", type=str, nargs="?", help="the markdown file to convert")
    parser.add_argument("-t", "--template", dest="template", type=str, help="the template to use")
    parser.add_argument("-o", "--output", dest="output", type=str, help="the output file")
    parser.add_argument("-f", "--format", dest="format", type=str, help="the output format")
    parser.add_argument("--", dest="extra", action="store", help="extra options passed to pandoc")
    args = parser.parse_args()

    if args.doc is None:
        parser.print_help()
        return

    template = TemplateClass(args.format or "latex")(args.template or "ascelike-new")
    template.render(args.doc, args.output, args.extra or "")


if __name__ == "__main__":
    cli()
