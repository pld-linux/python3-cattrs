#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Composable complex class support for attrs
Summary(pl.UTF-8):	Obsługa składanych klas złożonych dla attrs
Name:		python3-cattrs
Version:	1.10.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/cattrs/
Source0:	https://files.pythonhosted.org/packages/source/c/cattrs/cattrs-%{version}.tar.gz
# Source0-md5:	693fc2033e09019103bf2a184ba027f9
URL:		https://pypi.org/project/cattrs/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs >= 20
BuildRequires:	python3-pytest
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-typing_extensions
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
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

%prep
%setup -q -n cattrs-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/cattr
%{py3_sitescriptdir}/cattrs
%{py3_sitescriptdir}/cattrs-%{version}-py*.egg-info
