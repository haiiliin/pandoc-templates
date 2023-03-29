# ascelike-new: Template for Preparing Your Submission to the American Society Of Civil Engineers (ASCE)

This is a template for preparing your submission to the American Society Of Civil Engineers (ASCE). It is based on 
[ASCE LaTeX template](https://www.overleaf.com/latex/templates/template-for-preparing-your-submission-to-the-american-society-of-civil-engineers-asce/pbwcqsvndpty/).

## Metadata and Options

Options are set in the YAML header. The following options are available:

|       Key       |  Type  | Required |   Default    | Description                                                                        |
|:---------------:|:------:|:--------:|:------------:|------------------------------------------------------------------------------------|
| `documentclass` | string |    No    |  `Journal`   | Document class, e.g. `Journal`, `Proceedings` or `NewProceedings`                  |
|   `packages`    |  list  |    No    |     `[]`     | Packages to be loaded, list of dictionaries with keys `name`, `options`            |
|   `preamble`    | string |    No    |     `""`     | LaTeX code to be inserted in the preamble                                          |
|     `title`     | string |   Yes    |              | Title of the paper                                                                 |
|    `authors`    |  list  |   Yes    |              | Authors of the paper, list of dictionaries with keys `index`, `name`               |
| `affiliations`  |  list  |   Yes    |              | Affiliations of the authors, list of dictionaries with keys `index`, `affiliation` |
|    `nametag`    | string |   Yes    |              | Name tag of the paper, usually last name of the first author                       |
|   `abstract`    | string |   Yes    |              | Abstract of the paper                                                              |
|   `keywords`    |  list  |   Yes    |              | Keywords of the paper, list of strings                                             |
| `bibliography`  | string |   Yes    |              | Path to the bibliography (`*.bib`) file                                            |

## Example

```markdown
---
documentclass: Journal
packages:
  - name: filecontents
preamble: |
  \begin{filecontents*}{example.bib}
  @Article{key,
      author = {author},
      title  = {title},
  }
  \end{filecontents*}
title: Example Paper
authors:
  - index: 1
    name: Hai-Lin Wang
  - index: 1,*
    name: Zhen-Yu Yin
affiliations:
  - index: 1
    affiliation: Department of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong, China
nametag: Wang
abstract: |
  This is an example paper.
keywords:
    - example
    - paper
bibliography: example.bib
...

# Introduction

This is an example of a document written in Markdown and converted to LaTeX using Pandoc.
```

## Usage

Use the `ascelike-new` template to create a new paper:

```bash
pandoc --from markdown --to latex --template templates/ascelike-new --output ascelike-new.tex ascelike-new.md
```
