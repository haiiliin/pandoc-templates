# ascelike-new: Template for Preparing Your Submission to the American Society Of Civil Engineers (ASCE)

This is a template for preparing your submission to the American Society Of Civil Engineers (ASCE). It is based on 
[ASCE LaTeX template](https://www.overleaf.com/latex/templates/template-for-preparing-your-submission-to-the-american-society-of-civil-engineers-asce/pbwcqsvndpty/).

## Metadata and Options

Options are set in the YAML header. The following options are available:

| Key             | Type   | Required  | Default | Description                                                                        |
|-----------------|--------|-----------|---------|------------------------------------------------------------------------------------|
| `documentclass` | string | no        | Journal | Document class, e.g. `Journal`, `Proceedings` or `NewProceedings`                  |
| `packages`      | list   | no        |         | Packages to be loaded, list of dictionaries with keys `name`, `options`            |
| `preamble`      | string | no        |         | LaTeX code to be inserted in the preamble                                          |
| `title`         | string | yes       |         | Title of the paper                                                                 |
| `authors`       | list   | yes       |         | Authors of the paper, list of dictionaries with keys `index`, `name`               |
| `affiliations`  | list   | yes       |         | Affiliations of the authors, list of dictionaries with keys `index`, `affiliation` |
| `nametag`       | string | yes       |         | Name tag of the paper, usually last name of the first author                       |
| `abstract`      | string | yes       |         | Abstract of the paper                                                              |
| `keywords`      | list   | yes       |         | Keywords of the paper, list of strings                                             |
| `bibliography`  | string | yes       |         | Path to the bibliography (`*.bib`) file                                            |

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
