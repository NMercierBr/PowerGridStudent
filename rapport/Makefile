NAME1=Nom1_
NAME2=Nom2_
NAME3=Nom3

MATIERE=Python

PDFNAME=TP_$(MATIERE)_$(NAME1)$(NAME2)$(NAME3).pdf



all: main

main: main.tex
	pdflatex main.tex
	pdflatex main.tex

test: main
	open main.pdf

rename:
	mv main.pdf $(PDFNAME)
