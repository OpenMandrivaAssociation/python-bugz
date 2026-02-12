%define module pybugz
%define oname bugz

Name:		python-bugz
Summary:	A python and command line interface to Bugzilla
Version:	0.14
Release:	1
License:	GPL-2.0
Group:		Development/Python
URL:		https://github.com/williamh/pybugz
Source0:    %{URL}/archive/%{version}/%{name}-%version.tar.gz

BuildSystem:	python
BuildArch: noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
%{module} is a python and command line interface to Bugzilla.

It was conceived as a tool to speed up the workflow for Gentoo Linux developers
and contributors when dealing with bugs using Bugzilla. By avoiding the clunky
web interface, the user quickly search, isolate and contribute to the project
very quickly.

Developers alike can easily extract attachments and close bugs all from the 
comfort of the command line.

PyBugz is written in Python and written in a way to be extended easily for 
use on other Bugzillas.

%files
%doc README
%license LICENSE
%_bindir/%{oname}
%{_datadir}/pybugz.d/*.conf
%{_datadir}/bash-completion/completions/%{oname}
%{_datadir}/zsh/site-functions/_%{module}
%{_mandir}/man1/%{oname}*
%{_mandir}/man5/%{module}*
%{py_sitedir}/%{oname}/
%{py_sitedir}/%{module}-%{version}.dist-info
