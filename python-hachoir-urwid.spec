%define module_name hachoir-urwid

Summary:	The most sexy user interface based on hachoir-parser to explore a binary file
Name:		python-%{module_name}
Version:	1.1
Release:	%mkrel 1
Source0:	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://hachoir.org/wiki/hachoir-parser
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
%{py_requires -d}
BuildRequires:	python-setuptools

%description
hachoir-urwid  is a package with the most sexy user interface using hachoir-
core.  Not all parsers are complete, some are very good and other are poor:
only parse first level of the tree for example.

A perfect parser have no "raw" field: with a perfect parser you are able 
to know *each* bit meaning. Some good (but not perfect ;-)) parsers:

    * Matroska video
    * Microsoft RIFF (AVI video, WAV audio, CDA file)
    * PNG picture
    * TAR and ZIP archive 

%prep
%setup -q -n %{module_name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc AUTHORS COPYING README 
%dir %{py_puresitedir}/hachoir_urwid
