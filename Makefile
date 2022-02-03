# command to use to run python 
PYTHON = python3

# location of figures 
figdir = figs
# location of python source files 
PYSRC = python
# location of data files 
datadir = data
# location of standalone tikz files 
tikzdir = tikz

# location of matplotlibrc (makes plots look nice) 
MPL = matplotlibrc
# location of references file 
REF = references.bib

# name of main document 
MAIN = doc

# list of figures to be built for the document 
FIGS = 
FIGS := $(addsuffix .pdf, $(FIGS))

# list of tables to build
TABS = 
TABS := $(addsuffix .tex, $(TABS))
TABS := $(addprefix $(figdir)/, $(TABS))

# build all tex files in tikzdir directory 
TIKZ = $(notdir $(basename $(wildcard tikz/*.tex)))
TIKZ := $(addsuffix .pdf, $(TIKZ))

# search for .py dependencies in SRC directory 
vpath %.py $(PYSRC)
# also search for .pdf in figdir 
vpath %.pdf $(figdir)
# search for .tex dependencies in tikzdir 
vpath %.tex $(tikzdir) 

# generate figures, tables, and latex document 
.PHONY : all 
all : $(MAIN).pdf

# create a directory called $(figdir) if needed 
$(figdir) : 
	mkdir -p $(figdir)

# make figures from python code. save to figdir directory 
%.pdf : %.py $(MPL) $(datadir)/*
	$(PYTHON) $< $(figdir)/$@

# build tables from corresponding python code 
$(figdir)/%.tex : %.py $(datadir)/*
	$(PYTHON) $< $@ 

# build standalone TIKZ figures 
%.pdf : %.tex 
	@latexmk -pdf -output-directory=$(figdir) $< > /dev/null 

# compile latex with latexmk
$(MAIN).pdf: $(MAIN).tex $(figdir) $(FIGS) $(TABS) $(TIKZ) $(REF) *.tex Makefile
	@latexmk -pdf \
		-pdflatex="pdflatex --interaction=nonstopmode --shell-escape %O %S" \
		$(MAIN) > /dev/null

# list figure names 
listfigs : 
	@echo $(FIGS)
# list table names 
listtabs : 
	@echo $(TABS)
# list names of tikz targets 
listtikz : 
	@echo $(TIKZ)

# clear temp files associated with building in tikz directory 
.PHONY : 
cleantikz : 
	@$(foreach file, $(notdir $(basename $(TIKZ))), find $(tikzdir) -maxdepth 1 -type f -name '$(file).*' ! -name '$(file).tex' -delete;)
# clear aux files from figs directory 
.PHONY : 
cleanfigs : 
	@$(foreach file, $(notdir $(basename $(TIKZ))), find $(figdir) -maxdepth 1 -type f -name '$(file).*' ! -name '$(file).pdf' -delete;)
# remove auxiliary files associated with a tex file in the main directory
.PHONY : 
cleantex : 
	@$(foreach file, $(basename $(wildcard *.tex)), find . -maxdepth 1 -type f -name '$(file).*' ! -name '$(file).tex' -delete;)

# remove tex auxilary files 
.PHONY : clean 
clean : 
	rm -rf $(figdir) 
	rm -rf $(PYSRC)/__pycache__
	rm -rf __pycache__
	$(MAKE) cleantex 
	$(MAKE) cleantikz

# --- targets that require specific command line arguments --- 
