---
documentclass: Journal
packages:
  - name: filecontents
  - name: longtable
  - name: booktabs
  - name: multirow
  - name: array
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

This is an example paper.
