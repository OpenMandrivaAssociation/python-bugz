%define module_name pybugz
%define shortname bugz

Summary:    A python and command line interface to Bugzilla 
Name:		python-bugz
Version:    0.8.0
Release:	5
Source0:    http://pybugz.googlecode.com/files/pybugz-%version.tar.gz
Patch0:		pybugz-really-receive-auth-cookie.patch
Patch1:		pybugz-properly-modify-bugz.patch
Patch2:		pybugz-python2.7.patch
License:	GPL
Group:		Development/Python
Url:		https://code.google.com/p/pybugz/
BuildRequires: python-devel
BuildArch: noarch
Requires:  python-elementtree

%description
PyBugz is a python and command line interface to Bugzilla.

It was conceived as a tool to speed up the workflow for Gentoo Linux developers
and contributors when dealing with bugs using Bugzilla. By avoiding the clunky 
web interface, the user quickly search, isolate and contribute to the project 
very quickly. 
Developers alike can easily extract attachments and close bugs all from the 
comfort of the command line.

PyBugz is written in Python and written in a way to be extended easily for 
use on other Bugzillas.  

%prep
%setup -q -n %module_name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
perl -pi -e 's|http://bugs.gentoo.org/|https://qa.mandriva.com/|' bugz/cli.py

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README
%_bindir/bugz
%{py_sitedir}/%{shortname}/
%{py_sitedir}/%{module_name}-%{version}-py%{py_ver}.egg-info


%changelog
* Thu Nov 11 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.8.0-3mdv2011.0
+ Revision: 596171
- P2: fix issues with python 2.7
- Rebuild for new python.
  Explicitly define installed files.

* Tue Nov 10 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.8.0-1mdv2010.1
+ Revision: 464134
- P0: properly receive auth cookie
  P1: really modify bugs on newer bugzilla versions

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - new version 0.8.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.11-10mdv2010.0
+ Revision: 442045
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.6.11-9mdv2009.1
+ Revision: 323535
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.6.11-8mdv2009.0
+ Revision: 259510
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.11-7mdv2009.0
+ Revision: 247387
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.11-5mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.11-5mdv2008.0
+ Revision: 90199
- rebuild

* Sun Jul 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.11-4mdv2008.0
+ Revision: 54477
- Remove unused patch
- [BUGFIX] Add Patch 1 to fix bug  #31852 (thanks to Gustavo De Nardin)

* Mon May 14 2007 Michael Scherer <misc@mandriva.org> 0.6.11-3mdv2008.0
+ Revision: 26606
- add patch0, to make it work with python 2.5 and bundled elementtree


* Wed Dec 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.11-2mdv2007.0
+ Revision: 100501
- Rebuild against new python

* Wed Sep 27 2006 Michael Scherer <misc@mandriva.org> 0.6.11-1mdv2007.1
+ Revision: 62647
- add a Requires on python-elementtree, thanks titi for spotting this
- version 0.6.11
- Import python-bugz

* Fri Sep 22 2006 Michael Scherer <misc@mandriva.org> 0.6-1mdv2007.0
- first package

