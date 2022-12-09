# asce-new: Template for Preparing Your Submission to the American Society Of Civil Engineers (ASCE)

This is a template for preparing your submission to the American Society Of Civil Engineers (ASCE). It is based on the [ASCE LaTeX template](https://www.overleaf.com/latex/templates/template-for-preparing-your-submission-to-the-american-society-of-civil-engineers-asce/pbwcqsvndpty/).

## Metadata and Options

Options are set in the YAML header. The following options are available:

- `documentclass` (string, optional, by default `Journal`): Document class, e.g. `Journal`, `Proceedings` or `NewProceedings`
- `packages` (list of dictionaries with keys `name`, `options`, optional): Packages to be loaded
- `preamble` (string, optional): LaTeX code to be inserted in the preamble
- `title` (string, required): Title of the paper
- `authors` (list of dictionaries with keys `index`, `name`, required): Authors of the paper
- `affiliations` (list of dictionaries with keys `index`, `affiliation`, required): Affiliations of the authors
- `nametag` (string, required): Name tag of the paper, usually last name of the first author
- `abstract` (string, required): Abstract of the paper
- `keywords` (list of strings, required): Keywords of the paper
- `bibliography` (string, required): Path to the bibliography (`*.bib`) file

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
```

## Usage

Use the `asce-new` template to create a new paper:

```bash
pandoc --from markdown --to latex --template ascelike-new --output example.tex example.md
```
