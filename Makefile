# command to use to run python 
PYTHON = python3

# location of figures 
figdir = figs
# location of python source files 
pysrc = pysrc
# location of data files 
datadir = data
# location of standalone tikz files 
tikzdir = tikz
# location of tex subfiles 
subfiles_dir = chapters

# location of matplotlibrc (makes plots look nice) 
MPL = matplotlibrc
# location of references file 
REF = references.bib
# location of glossary file 
GLOSS = glossary.tex
# location of dissertation class file 
CLS = dissertation.cls

# name of main document 
MAIN = doc

# list of figures to be built for the document 
FIGS = lor lor4 lor8 lor_dist lor_dist4 lor_dist8 conj_grad \
sweep eps_lineout quad_mesh sparse1d reentrant normal \
dgvef/mms dgvef/unified rtvef/hyb_sparsity smm/mms \
disc/iguess disc/ciguess
FIGS := $(addsuffix .pdf, $(FIGS))

# list of tables to build
TABS = cp eps_table\
dgvef/weak dgvef/mock dgvef/mms_table\
rtvef/weak rtvef/solvers rtvef/mms rtvef/mms_elev rtvef/mms_diff \
smm/weak smm/vmms smm/mms_diff smm/mms_elev \
disc/anderson disc/eps3 disc/eps_all allweak
TABS := $(addsuffix .tex, $(TABS))
TABS := $(addprefix $(figdir)/, $(TABS))

# build all tex files in tikzdir directory 
TIKZ = $(notdir $(basename $(wildcard tikz/*.tex)))
TIKZ := $(addsuffix .pdf, $(TIKZ))

# search for .py dependencies in SRC directory 
vpath %.py $(pysrc)
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
	mkdir -p $(figdir)/dgvef $(figdir)/rtvef $(figdir)/smm $(figdir)/disc

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
$(MAIN).pdf: $(MAIN).tex $(figdir) $(FIGS) $(TABS) $(TIKZ) $(REF) $(GLOSS) $(CLS) $(subfiles_dir)/*.tex Makefile
	@latexmk -pdf \
		-pdflatex="pdflatex --interaction=nonstopmode --shell-escape %O %S" \
		$(MAIN) > /dev/null

# compile chapters individually 
% : $(subfiles_dir)/%.tex $(figdir) $(FIGS) $(TABS) $(TIKZ) $(REF) $(GLOSS) $(CLS) Makefile 
	cd $(subfiles_dir); latexmk -pdf $@ > /dev/null

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
# remove auxiliary files associated with a tex file in the main and subfiles directories
.PHONY : 
cleantex : 
	@$(foreach dir, . $(subfiles_dir),\
		$(foreach file, $(notdir $(basename $(wildcard $(dir)/*.tex))),\
			find $(dir) -maxdepth 1 -type f -name '$(file).*' ! -name '$(file).tex' -delete;))

# remove tex auxilary files 
.PHONY : clean 
clean : 
	rm -rf $(figdir) 
	rm -rf $(pysrc)/__pycache__
	rm -rf __pycache__
	$(MAKE) cleantex 
	$(MAKE) cleantikz

# --- targets that require specific command line arguments --- 
# low order refined diagrams 
lor4.pdf : lor.py $(MPL) 
	$(PYTHON) $< $(figdir)/$@ 4
lor8.pdf : lor.py $(MPL) 
	$(PYTHON) $< $(figdir)/$@ 8
lor_dist4.pdf : lor_dist.py $(MPL) 
	$(PYTHON) $< $(figdir)/$@ 4 
lor_dist8.pdf : lor_dist.py $(MPL) 
	$(PYTHON) $< $(figdir)/$@ 8

# MMS on various directories 
$(figdir)/rtvef/mms_elev.tex : $(pysrc)/rtvef/mms.py 
	$(PYTHON) $< $@ data/rtvef/mms_elev/
$(figdir)/rtvef/mms_diff.tex : $(pysrc)/rtvef/mms.py 
	$(PYTHON) $< $@ data/rtvef/mms_diff/
$(figdir)/smm/mms_elev.tex : $(pysrc)/smm/vmms.py 
	$(PYTHON) $< $@ data/smm/mms_elev/
$(figdir)/smm/mms_diff.tex : $(pysrc)/smm/vmms.py 
	$(PYTHON) $< $@ data/smm/mms_diff/

# plot cumulative inner solves for initial guess comparison 
$(figdir)/disc/ciguess.pdf : $(pysrc)/disc/iguess.py $(MPL) 
	$(PYTHON) $< $@ 1