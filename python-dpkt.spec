# TODO: process docs to HTML?
#
# Conditional build:
%bcond_without	doc	# Markdown documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
Summary(pl.UTF-8):	Szybkie, proste tworzenie i analiza pakietów z definicjami podstawowych protokołów TCP/IP
Name:		python-dpkt
Version:	1.9.7.2
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/dpkt/
Source0:	https://files.pythonhosted.org/packages/source/d/dpkt/dpkt-%{version}.tar.gz
# Source0-md5:	ac3ace1c5ee12a74f12a863ac9082b59
URL:		https://pypi.org/project/dpkt/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-pytest-cov
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The dpkt project is a Python module for fast, simple packet parsing,
with definitions for the basic TCP/IP protocols.

%description -l pl.UTF-8
Projekt dpkt to moduł Pythona do szybkiego, prostego analizowania
pakietów, wraz z definicjami podstawowych protokołów TCP/IP.

%package -n python3-dpkt
Summary:	Fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols
Summary(pl.UTF-8):	Szybkie, proste tworzenie i analiza pakietów z definicjami podstawowych protokołów TCP/IP
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-dpkt
The dpkt project is a Python module for fast, simple packet parsing,
with definitions for the basic TCP/IP protocols.

%description -n python3-dpkt -l pl.UTF-8
Projekt dpkt to moduł Pythona do szybkiego, prostego analizowania
pakietów, wraz z definicjami podstawowych protokołów TCP/IP.

%package apidocs
Summary:	API documentation for Python dpkt module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona dpkt
Group:		Documentation

%description apidocs
API documentation for Python dpkt module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona dpkt.

%prep
%setup -q -n dpkt-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_cov.plugin" \
%{__python} -m pytest dpkt
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_cov.plugin" \
%{__python3} -m pytest dpkt
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{py_sitescriptdir}/dpkt
%{py_sitescriptdir}/dpkt-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-dpkt
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{py3_sitescriptdir}/dpkt
%{py3_sitescriptdir}/dpkt-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/*
%endif
