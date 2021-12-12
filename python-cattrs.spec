#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-cattrs.spec)

Summary:	Composable complex class support for attrs
Summary(pl.UTF-8):	Obsługa składanych klas złożonych dla attrs
Name:		python-cattrs
# keep 1.0.x here for python2 support
Version:	1.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cattrs/
Source0:	https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
# Source0-md5:	c57222f5475f0158d2bffb87ac1411f9
URL:		https://pypi.org/project/cattrs/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-attrs >= 17.3
BuildRequires:	python-enum34 >= 1.1.6
BuildRequires:	python-functools32 >= 3.2.3
BuildRequires:	python-pytest
BuildRequires:	python-singledispatch >= 3.4.0.3
BuildRequires:	python-typing >= 3.5.3
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs >= 17.3
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.

%description -l pl.UTF-8
cattrs to mająca otwarte źródła biblioteka Pythona do strukturyzacji i
destrukturyzacji danych. Najlepiej działa z klasami attrs oraz
zwykłymi kolekcjami Pythona, ale inne rodzaje klas są obsługiwane
poprzez ręcznie rejestrowane konwertery.

%package -n python3-cattrs
Summary:	Composable complex class support for attrs
Summary(pl.UTF-8):	Obsługa składanych klas złożonych dla attrs
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-cattrs
cattrs is an open source Python library for structuring and
unstructuring data. cattrs works best with attrs classes and the usual
Python collections, but other kinds of classes are supported by
manually registering converters.

%description -n python3-cattrs -l pl.UTF-8
cattrs to mająca otwarte źródła biblioteka Pythona do strukturyzacji i
destrukturyzacji danych. Najlepiej działa z klasami attrs oraz
zwykłymi kolekcjami Pythona, ale inne rodzaje klas są obsługiwane
poprzez ręcznie rejestrowane konwertery.

%package apidocs
Summary:	API documentation for Python cattrs module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cattrs
Group:		Documentation

%description apidocs
API documentation for Python cattrs module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cattrs.

%prep
%setup -q -n cattrs-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
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
%doc HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/cattr
%{py_sitescriptdir}/cattrs-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-cattrs
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/cattr
%{py3_sitescriptdir}/cattrs-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
