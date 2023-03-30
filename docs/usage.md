# Basic Usage

This page describes how to use the the `pandoc-templates` project to set up our own workflow for creating LaTeX documents 
by markdown files using [Pandoc](https://pandoc.org/).

## Generate the repository from the template

The first step is to generate a new repository from the template. This can be done by clicking on the 
`Use this template` button on the [GitHub repository](https://github.com/haiiliin/pandoc-templates/).
```{image} /images/use-this-template.png
:width: 50%
```

Fill in the repository name and description and click on `Create repository from template`.
```{image} /images/create-repository-from-template.png
:width: 100%
```

## Remove unnecessary files

An automated workflow `.github/workflows/cleanup-template.yml` is set up to remove unnecessary files from the repository. 
This workflow is triggered when a new repository is created from the template. Because the GitHub workflow does not
have access to write to the repository, the workflow will fail. To fix this, go to the `Settings` tab of the repository
and click on `Actions` and `General` in the left menu. Then select `Read and write permissions` for the `Actions` in
the `Workflow permissions` section.
```{image} /images/workflow-permissions.png
:width: 100%
```

Go the project home page and click on the `Actions` tab. Then click on the `GitHub Template` workflow, select the 
failed run and click on `Re-run jobs`.
```{image} /images/re-run-jobs.png
:width: 30%
```
After the workflow has finished, the unnecessary files should be removed from the repository.

## Generate the main document from the template

To generate the main document from the template, go to the project's `Actions` tab and click on the `Manuscript` 
workflow. Select the branch, template, manuscript file name and click on the `Run workflow` button.
```{image} /images/run-manuscript-workflow.png
:width: 50%
```
After the workflow has finished, a markdown file with the manuscript name should be created in the root of the 
repository. 

## Clone the repository and make changes to the manuscript

Clone the repository to your local machine and make any changes to the manuscript file. Then commit and push the changes
to the repository. Use the [Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown) syntax for the 
manuscript file.

## Generate the PDF document

To generate the PDF document, go to the project's `Actions` tab and click on the `Compile` workflow. Select the branch,
template, manuscript file name, LaTeX compiler and click on the `Run workflow` button.
```{image} /images/run-compile-workflow.png
:width: 50%
```
After the workflow has finished, a zip file with the PDF document should be created in the `artifacts` section of the
workflow run.
```{image} /images/artifacts.png
:width: 100%
```

## Compile the document locally

To compile the document locally, you need to have a LaTeX distribution (e.g. [TeX Live](https://www.tug.org/texlive/))
and [Pandoc](https://pandoc.org/) installed on your machine.

Copy the required template files from the `templates/{template}` directory to the root of the repository (usually
only `*.cls`, `*.sty`, and `*.bst` files are required). Then run the following command in the root of the repository:
```bash
pandoc --from markdown --to latex --template templates/{template} --output manuscript.tex manuscript.md
```
