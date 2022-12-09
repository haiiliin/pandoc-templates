import argparse

from .template import PandocTemplate


def cli():
    parser = argparse.ArgumentParser(prog="pypandoctemplates", description="pypandoctemplates command line interface")
    parser.add_argument("doc", metavar="doc", type=str, nargs="?", help="The markdown file to convert")
    parser.add_argument("-f", "--from", "-r", "--read", dest="from", type=str, help="Specify input format")
    parser.add_argument("-t", "--to", "-w", "--write", dest="to", type=str, help="Specify output format")
    parser.add_argument("-o", "--output", dest="output", type=str, help="Write output to FILE instead of stdout")
    parser.add_argument("--template", dest="template", type=str, help="Use a custom template")
    parser.add_argument("-s", "--standalone", dest="standalone", type=bool, help="Wrap output in a standalone document")
    parser.add_argument("--data-dir", dest="data_dir", type=str, help="Specify the user data directory")
    parser.add_argument("-d", "--defaults", dest="defaults", type=str, help="Specify a set of default option settings")
    parser.add_argument("--", dest="extra", action="store", type=str, help="extra options passed to pandoc")

    args = parser.parse_args()
    PandocTemplate(**vars(args)).render()


if __name__ == "__main__":
    cli()
