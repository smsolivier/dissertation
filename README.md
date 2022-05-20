# High-Order Moment Methods for Thermal Radiative Transfer
This repository contains the source files for building my PhD dissertation. This includes Latex files for the text of the document and many of the figures generated via Tikz as well as python scripts to process and procedurally generate the figures and tables associated with the data from numerical results. 

The compiled document is freely available at [link](http://samolivier.net/wp-content/uploads/dissertation.pdf).

## Key Features 
* `Make` controls processing experimental data and procedurally generating figures and tables as well as building the document itself 
	* Can build individual chapters to reduce the expense of compiling a large document 
	* provides targets to clean auxiliary tex files 
	* allows amortizing the cost of compiling Tikz figures by building them to PDF and then including the PDF in the document 
	* avoids the need to track figures and tables (that may be changing as you generate results) 
* each chapter is in its own `.tex` file (I used the `subfiles` Latex package) 
	* adding `% !TEX root = ../doc.tex` to the top of each subfile tells editors (e.g. Sublime Text) to use citation and equation references from the entire document 
* formatting and common macros stored in separate class file (`dissertation.cls`) which extends the `ucbthesis` Latex class. This declutters the main `doc.tex` file. 
* `matplotlibrc` makes sure all figures generated with `python` have the same settings and formatting 
* `.latexmkrc` ensures the glossary is built properly using the `latexmk` utility from TexLive 

## Building the Document
Build dependencies: 
* `Make`
* `latexmk` (included with TexLive)
* `find` 

Some of the python scripts also depend on my: 
* [1D transport finite element code](https://github.com/smsolivier/pytrans1d)
* [2D transport finite element code](https://github.com/smsolivier/pytrans2d)

These can be installed by running `pip install .` in the root directory of the repos. Also, my [PythonScripts](https://github.com/smsolivier/PythonScripts) repo should be in your `PYTHONPATH` (e.g. using the `export` bash command).

With these dependencies, the document can be built by running `make` in the root directory. This command will run `latexmk` on each of the figures in the `tikz` directory and run `python3` on the targets associated with the `pysrc` directory. These tables and figures are output into a directory called `figs`. Finally, the document itself is generated using `latexmk`. The auxiliary latex files and procedurally generated tables and figures can be removed by running `make clean` in the root directory. 

Individual chapters can be built with 
```
make <name_of_chapter>
```
where `name_of_chapter` is the basename of a `.tex` file in the `chapters` directory. Note that the built document for that chapter will be located in the `chapters` directory. The `chapters` directory can be cleaned without deleting the `figs` directory using `make cleantex` from the root directory. 

## Description of Files
* `chapters`: directory for storing subfiles corresponding to each chapter 
* `data'`: contains numerical results and images that are not procedurally generated with python 
* `pysrc`: python scripts used to generate tables and figures 
* `tikz`: standalone Tikz figures 
* `Makefile`: contains all targets and variables to set the names of the above directories 
* `dissertation.cls`: custom class file with additional formatting and commands 
* `doc.tex`: main file for the document
* `glossary.tex`: list of acronyms used in the document (for the `glossaries` Latex package) 
* `.latexmkrc`: settings file for `latexmk` used to include running `makeglossaries` into `latexmk` 
* `matplotlibrc`: settings file for matplotlib
* `references.bib`: citation information 
* `ucbthesis.cls`: UC Berkeley dissertation class provided by [Paul Vojta](https://math.berkeley.edu/~vojta/tex/ucbthesis-phd.html)

## Useful Links
* [UCB Dissertation Requirements](https://grad.berkeley.edu/academic-progress/doctoral/dissertation/)
