# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the $(SPHINXBUILD) executable. Alternatively you can add the directory with the Sphinx executable to your PATH. If you don't have Sphinx installed, fetch it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)
ALLSPHINXOPTS   := $(filter-out -D latex_paper_size=, $(ALLSPHINXOPTS)) $(PAPEROPT_$(PAPER))

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man texinfo linkcheck doctest coverage

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a Windows help project"
	@echo "  qthelp     to make HTML files and a Qt help project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an EPUB file"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX PDF files, you can set PAPER=a4 or PAPER=letter"
	@echo "  text       to make text files"
	@echo "  man        to make manual page files"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  xml        to make Docutils-native XML files"
	@echo "  pseudoxml  to make pseudoxml-native XML files"
	@echo "  linkcheck  to make a linkcheck of all external links"
	@echo "  doctest    to make all doctests in the documentation"
	@echo "  coverage   to make a coverage check of the documentation"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) . $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML documentation is in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) . $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML documentation is in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) . $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML documentation is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) . $(BUILDDIR)/pickle
	@echo
	@echo "Build finished. The Pickle files are in $(BUILDDIR)/pickle."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) . $(BUILDDIR)/json
	@echo
	@echo "Build finished. The JSON files are in $(BUILDDIR)/json."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) . $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished. The HTML help files are in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) . $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished. The HTML help files are in $(BUILDDIR)/qthelp."

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) . $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished. The HTML help files are in $(BUILDDIR)/devhelp."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) . $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The EPUB file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) . $(BUILDDIR)/latex
	@echo
	@echo "Build finished. The LaTeX files are in $(BUILDDIR)/latex."

latexpdf:
	$(SPHINXBUILD) -b latexpdf $(ALLSPHINXOPTS) . $(BUILDDIR)/latex
	@echo
	@echo "Build finished. The PDF file is in $(BUILDDIR)/latex/GestorVideojuegos.pdf."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) . $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) . $(BUILDDIR)/man
	@echo
	@echo "Build finished. The man page files are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) . $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) . $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make info' in the $(BUILDDIR)/texinfo directory."

gettext:
	$(SPHINXBUILD) -b gettext $(I18N_TEXDIR) $(BUILDDIR)/gettext
	@echo
	@echo "Build finished. The gettext files are in $(BUILDDIR)/gettext."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) . $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

xml:
	$(SPHINXBUILD) -b xml $(ALLSPHINXOPTS) . $(BUILDDIR)/xml
	@echo
	@echo "Build finished. The XML files are in $(BUILDDIR)/xml."

pseudoxml:
	$(SPHINXBUILD) -b pseudoxml $(ALLSPHINXOPTS) . $(BUILDDIR)/pseudoxml
	@echo
	@echo "Build finished. The pseudoxml files are in $(BUILDDIR)/pseudoxml."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) . $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for output in $(BUILDDIR)/linkcheck/index.html."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) . $(BUILDDIR)/doctest
	@echo
	@echo "The doctest file is in $(BUILDDIR)/doctest."

coverage:
	$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) . $(BUILDDIR)/coverage
	@echo
	@echo "The coverage file is in $(BUILDDIR)/coverage."
