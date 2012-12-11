%define module_name hachoir-urwid

Summary:	The most sexy user interface based on hachoir-parser to explore a binary file
Name:		python-%{module_name}
Version:	1.1
Release:	%mkrel 2
Source0:	http://cheeseshop.python.org/packages/source/h/%{module_name}/%{module_name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://hachoir.org/wiki/hachoir-parser
BuildArch:	noarch
Requires:	python-hachoir-core
Requires:	python-hachoir-parser
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

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/*
%{py_puresitedir}/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.1-2mdv2011.0
+ Revision: 598271
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2010.0
+ Revision: 442180
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.1-1mdv2009.1
+ Revision: 320023
- rebuild with python 2.6
- clean spec
- new release 1.1

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 259628
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 247430
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 166729
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 17 2007 Jérôme Soyer <saispo@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 52870
- New release 1.0.1
- Import python-hachoir-urwid

