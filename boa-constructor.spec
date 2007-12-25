%define		_ver beta
Summary:	Boa Constructor - a cross platform Python IDE
Summary(pl.UTF-8):	Boa Constructor - wieloplatformowe IDE do Pythona
Name:		boa-constructor
Version:	0.6.1
Release:	0.%{_ver}.1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/boa-constructor/%{name}-%{version}.src.zip
# Source0-md5:	150d923c608a405eeb17bf655ce26b14
#		boa-constructor-0.4.0.src.zip
URL:		http://boa-constructor.sourceforge.net/
BuildRequires:	ImageMagick
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

convert Images/Icons/Boa.ico -format png ./Boa.png
 
cat <<'EOF' > Boa.desktop
[Desktop Entry]
Name=Boa-Construktor
Comment=Cross platform Python IDE and wxPython GUI
Comment[pl]=Wieloplatformowe IDE do Pythona oraz narzędzie do budowania GUI
Icon=Boa.png
Exec=boa
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Development;IDE;
# vi: encoding=utf-8
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_examplesdir}/%{name}}

install Boa.png $RPM_BUILD_ROOT%{_pixmapsdir}
install Boa.desktop $RPM_BUILD_ROOT%{_desktopdir}
install *.py* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r bcrtl Companions Config Debugger Docs Explorers ExternalLib Images \
	Models Plug-ins PropEdit Views ZopeLib $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r Examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
find  $RPM_BUILD_ROOT%{_datadir}/%{name} -maxdepth 2 -name "*.py" | xargs rm

echo -e "#!/bin/sh
cd %{_datadir}/%{name}
python Boa.pyc" > $RPM_BUILD_ROOT%{_bindir}/boa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_examplesdir}/%{name}
%{_pixmapsdir}/Boa.png
%{_desktopdir}/Boa.desktop
