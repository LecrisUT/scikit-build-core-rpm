Name:		    pyhton-scikit-build-core
Version:	    0.1.6
Release:        1%{?dist}
Summary:	    Build backend for CMake based projects

License:	    ASL 2.0
URL:		    https://github.com/scikit-build/scikit-build-core
Source0:	    %{pypi_source scikit_build_core}

BuildArch:	    noarch
BuildRequires:	python3-devel
BuildRequires:	python3dist(hatchling)
BuildRequires:	python3dist(hatch-vcs)
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       cmake
# TODO: Removed in 0.1.7
Requires:	    python3dist(distlib)
Requires:	    python3dist(pyproject-metadata)
Requires:	    python3dist(pathspec)

%global _description %{expand:
A next generation Python CMake adaptor and Python API for plugins}

%description %_description

%package -n python3-scikit-build-core
Summary:	%{summary}
%description -n python3-scikit-build-core %_description

%prep
%autosetup -p1 -n scikit_build_core-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files scikit_build_core


%check
%pytest


%files -n python3-scikit-build-core -f %{pyproject_files}
%license

%changelog
%autochangelog

