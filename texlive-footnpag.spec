%global tl_name footnpag
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Per-page numbering of footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footnpag
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footnpag.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allows footnotes on individual pages to be numbered from 1, rather than
being numbered sequentially through the document.

