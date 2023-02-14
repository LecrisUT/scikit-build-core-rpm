# TODO: temporarily build from forgeurl
%global forgeurl https://github.com/scikit-build/scikit-build-core
%global branch main

Name:		    python-scikit-build-core
Version:	    0.1.6
Release:        1%{?dist}
Summary:	    Build backend for CMake based projects
%forgemeta

License:	    ASL 2.0
URL:		    %{forgeurl}
Source0:	    %{forgesource}

BuildArch:	    noarch
BuildRequires:	python3-devel
BuildRequires:	python3dist(hatchling)
BuildRequires:	python3dist(hatch-vcs)
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       cmake
Requires:	    python3dist(pyproject-metadata)
Requires:	    python3dist(pathspec)

%global _description %{expand:
A next generation Python CMake adaptor and Python API for plugins}

%description %_description

%package -n python3-scikit-build-core
Summary:	%{summary}
%description -n python3-scikit-build-core %_description

%prep
%forgesetup -v

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

