Summary:	Boa Constructor is a cross platform Python IDE
Name:		boa-constructor
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/boa-constructor/%{name}-%{version}.zip
# Source0-md5:	4e6097108e5a242ffd41292d1ac0ae75
URL:		http://boa-constructor.sourceforge.net/
Requires:	python-wxPython >= 2.4
Requires:	python-wxPython < 2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boa Constructor is a cross platform Python IDE and wxPython GUI
Builder. It offers visual frame creation and manipulation, an object
inspector, many views on the source like object browsers, inheritance
hierarchies, doc string generated html documentation, an advanced
debugger and integrated help.

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
