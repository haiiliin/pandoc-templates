# Examples

A manuscript is composed of a YAML header and a body. The YAML header contains the metadata of the manuscript,
such as the title, authors, affiliations, and abstract. The body contains the content of the manuscript, such as the 
introduction, methods, and results. The body is written in Markdown, a simple markup language. The YAML header is 
written in YAML, a simple data serialization language. The YAML header is separated from the body by three dashes `---`.
Detailed metadata of the manuscript specified in the YAML header is explained in the template description.
Here is an example of a simple manuscript:
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
---

# Introduction

This is an example of a document written in Markdown and converted to LaTeX using Pandoc.
```

The compiled PDF file of the example manuscript is available {download}`here <_static/pdf/manuscript.pdf>`.
