Summary:	Boa Constructor - a cross platform Python IDE
Summary(pl):	Boa Constructor - wieloplatformowe IDE do Pythona
Name:		boa-constructor
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/boa-constructor/%{name}-%{version}.src.zip
# Source0-md5:	4de080793412c5d57324b4f7f5ec3e79
#		boa-constructor-0.4.0.src.zip
URL:		http://boa-constructor.sourceforge.net/
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

%description -l pl
Boa Constructor to wieloplatformowe IDE do Pythona oraz narz�dzie do
budowania GUI opartych o bibliotek� wxPython. Oferuje wizualne
tworzenie i obr�bk� ramek, inspektora obiekt�w, wiele widok�w �r�de�,
takich jak przegl�darki obiekt�w, hierarchie dziedziczenia,
dokumentacj� HTML generowan� z �a�cuch�w doc oraz zaawansowany
debugger i zintegrowan� pomoc.

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
