%define module_name pybugz
%define shortname bugz

%define name python-bugz
%define release		%mkrel 3
Summary:    A python and command line interface to Bugzilla 
Name:		%name
Version:    0.8.0
Release:	%release
Source0:    http://pybugz.googlecode.com/files/pybugz-%version.tar.gz
Patch0:		pybugz-really-receive-auth-cookie.patch
Patch1:		pybugz-properly-modify-bugz.patch
Patch2:		pybugz-python2.7.patch
License:	GPL
Group:		Development/Python
Url:		http://code.google.com/p/pybugz/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc README
%_bindir/bugz
%{py_sitedir}/%{shortname}/
%{py_sitedir}/%{module_name}-%{version}-py%{pyver}.egg-info
