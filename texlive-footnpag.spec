Name:		texlive-footnpag
Version:	15878
Release:	2
Summary:	Per-page numbering of footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footnpag
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows footnotes on individual pages to be numbered from 1,
rather than being numbered sequentially through the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/footnpag/footnpag.sty
%doc %{_texmfdistdir}/doc/latex/footnpag/CATALOG
%doc %{_texmfdistdir}/doc/latex/footnpag/History
%doc %{_texmfdistdir}/doc/latex/footnpag/INSTALL
%doc %{_texmfdistdir}/doc/latex/footnpag/Imakefile
%doc %{_texmfdistdir}/doc/latex/footnpag/License
%doc %{_texmfdistdir}/doc/latex/footnpag/MANIFEST
%doc %{_texmfdistdir}/doc/latex/footnpag/README
%doc %{_texmfdistdir}/doc/latex/footnpag/TODO
%doc %{_texmfdistdir}/doc/latex/footnpag/footnpag-doc.sty
%doc %{_texmfdistdir}/doc/latex/footnpag/footnpag-user.pdf
%doc %{_texmfdistdir}/doc/latex/footnpag/footnpag-user.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/footnpag.doc
%doc %{_texmfdistdir}/doc/latex/footnpag/test/Imakefile
%doc %{_texmfdistdir}/doc/latex/footnpag/test/eqnarray-fnmark.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/test/late.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/test/many.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/test/minipage.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/test/report.tex
%doc %{_texmfdistdir}/doc/latex/footnpag/test/title-2col.tex
#- source
%doc %{_texmfdistdir}/source/latex/footnpag/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
