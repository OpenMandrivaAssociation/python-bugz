%define module_name pybugz

%define name python-bugz
%define release		%mkrel 1
Summary:    A python and command line interface to Bugzilla 
Name:		%name
Version:    0.8.0
Release:	%release
Source0:    http://pybugz.googlecode.com/files/pybugz-%version.tar.gz
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
perl -pi -e 's|http://bugs.gentoo.org/|http://qa.mandriva.com/|' bugz/cli.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES 
%defattr(-,root,root) 
%doc README


