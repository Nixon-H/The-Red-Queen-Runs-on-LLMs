# Submission package

This folder contains the files required to rebuild the current `main.pdf`:

- `main.tex`
- `refs.bib`
- `IEEEtran.cls`
- `IEEEtran.bst`
- `figures/`

`main.pdf` is the current compiled submission output. The two additional
Markdown files are submission-support documents. The CSV files, evidence
notes, corpus records, and reference sources remain in the parent research
repository because they are not LaTeX build dependencies.

## Rebuild

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
