# TODO: temporarily build from forgeurl
%global forgeurl https://github.com/scikit-build/scikit-build-core

Name:		    python-scikit-build-core
Version:	    0.2.0
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
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
Recommends:     (ninja-build or make)
Suggests:       gcc
Suggests:       clang
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
%pytest \
    -m "not isolated"


%files -n python3-scikit-build-core -f %{pyproject_files}
%license

%changelog
%autochangelog

