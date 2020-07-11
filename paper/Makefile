
all: mlt-template-2015.pdf

#%.pdf: %.tex mlt-thesis-2015.sty
#	lualatex $<; bibtex $*; lualatex $<; lualatex $<

%.pdf: %.tex mlt-thesis-2015.sty
	xelatex $<; bibtex $*; xelatex $<; xelatex $<

clean:
	rm -f *.log *.dvi *.aux *~ *.toc *.bbl *.blg mlt-template-2015.pdf
