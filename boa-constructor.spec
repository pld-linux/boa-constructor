Summary:	Boa Constructor - a cross platform Python IDE
Summary(pl.UTF-8):	Boa Constructor - wieloplatformowe IDE do Pythona
Name:		boa-constructor
Version:	0.4.4
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/boa-constructor/%{name}-%{version}.zip
# Source0-md5:	16d3384744e683e982907caef9f76c98
#		boa-constructor-0.4.0.src.zip
URL:		http://boa-constructor.sourceforge.net/
BuildRequires:	unzip
Requires:	python-wxPython > 2.4
#Requires:	python-wxPython < 2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boa Constructor is a cross platform Python IDE and wxPython GUI
Builder. It offers visual frame creation and manipulation, an object
inspector, many views on the source like object browsers, inheritance
hierarchies, doc string generated HTML documentation, an advanced
debugger and integrated help.

%description -l pl.UTF-8
Boa Constructor to wieloplatformowe IDE do Pythona oraz narzędzie do
budowania GUI opartych o bibliotekę wxPython. Oferuje wizualne
tworzenie i obróbkę ramek, inspektora obiektów, wiele widoków źródeł,
takich jak przeglądarki obiektów, hierarchie dziedziczenia,
dokumentację HTML generowaną z łańcuchów doc oraz zaawansowany
debugger i zintegrowaną pomoc.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install *.py* $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -r bcrtl Companions Config Debugger Docs Examples Explorers ExternalLib Images \
	Models Plug-ins PropEdit Views ZopeLib $RPM_BUILD_ROOT%{_datadir}/%{name}

echo -e "#!/bin/sh
cd %{_datadir}/%{name}
python Boa.py" > $RPM_BUILD_ROOT%{_bindir}/boa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
