# ascelike-new: Template for Preparing Your Submission to the American Society Of Civil Engineers (ASCE)

This is a template for preparing your submission to the American Society Of Civil Engineers (ASCE). It is based on 
[ASCE LaTeX template](https://www.overleaf.com/latex/templates/template-for-preparing-your-submission-to-the-american-society-of-civil-engineers-asce/pbwcqsvndpty/).

## Metadata and Options

Options are set in the YAML header. The following options are available:

|       Key       |  Type  | Required |   Default    | Description                                                                                    |
|:---------------:|:------:|:--------:|:------------:|------------------------------------------------------------------------------------------------|
| `documentclass` | string |    No    |  `Journal`   | Document class, e.g. `Journal`, `Proceedings` or `NewProceedings`                              |
|   `packages`    |  list  |    No    |     `[]`     | Packages to be loaded, list of dictionaries with keys `name`, `options`, `options` is optional |
|   `preamble`    | string |    No    |     `""`     | LaTeX code to be inserted in the preamble                                                      |
|     `title`     | string |   Yes    |              | Title of the paper                                                                             |
|    `authors`    |  list  |   Yes    |              | Authors of the paper, list of dictionaries with keys `index`, `name`                           |
| `affiliations`  |  list  |   Yes    |              | Affiliations of the authors, list of dictionaries with keys `index`, `affiliation`             |
|    `nametag`    | string |   Yes    |              | Name tag of the paper, usually last name of the first author                                   |
|   `abstract`    | string |   Yes    |              | Abstract of the paper                                                                          |
|   `keywords`    |  list  |   Yes    |              | Keywords of the paper, list of strings                                                         |
| `bibliography`  | string |   Yes    |              | Path to the bibliography (`*.bib`) file                                                        |

## Required Files

Please make sure that the following files are in the same directory as the Markdown file:

- [ascelike-new.cls](ascelike-new.cls): LaTeX class file 
- [ascelike-new.bst](ascelike-new.bst): BibTeX style file
- [ascelike-new.latex](/templates/ascelike-new.latex): Pandoc LaTeX template file
