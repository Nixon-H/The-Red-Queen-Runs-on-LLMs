#!/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "Building main.pdf..."
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex

echo "Cleaning intermediates..."
rm -f main.aux main.bbl main.blg main.log main.out

echo "Done: main.pdf"
