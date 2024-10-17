Name:		texlive-babel-indonesian
Version:	43235
Release:	2
Summary:	Support for Indonesian within babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-indonesian
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-indonesian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-indonesian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-indonesian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the babel style for Indonesian.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-indonesian
%{_texmfdistdir}/tex/generic/babel-indonesian
%doc %{_texmfdistdir}/doc/generic/babel-indonesian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
