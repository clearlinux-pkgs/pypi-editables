#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-editables
Version  : 0.5
Release  : 18
URL      : https://files.pythonhosted.org/packages/37/4a/986d35164e2033ddfb44515168a281a7986e260d344cf369c3f52d4c3275/editables-0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/4a/986d35164e2033ddfb44515168a281a7986e260d344cf369c3f52d4c3275/editables-0.5.tar.gz
Summary  : Editable installations
Group    : Development/Tools
License  : MIT
Requires: pypi-editables-license = %{version}-%{release}
Requires: pypi-editables-python = %{version}-%{release}
Requires: pypi-editables-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# A Python library for creating "editable wheels"
This library supports the building of wheels which, when installed, will
expose packages in a local directory on `sys.path` in "editable mode". In
other words, changes to the package source will be  reflected in the package
visible to Python, without needing a reinstall.

%package license
Summary: license components for the pypi-editables package.
Group: Default

%description license
license components for the pypi-editables package.


%package python
Summary: python components for the pypi-editables package.
Group: Default
Requires: pypi-editables-python3 = %{version}-%{release}

%description python
python components for the pypi-editables package.


%package python3
Summary: python3 components for the pypi-editables package.
Group: Default
Requires: python3-core
Provides: pypi(editables)

%description python3
python3 components for the pypi-editables package.


%prep
%setup -q -n editables-0.5
cd %{_builddir}/editables-0.5
pushd ..
cp -a editables-0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690232590
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-editables
cp %{_builddir}/editables-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-editables/4caad070b55cf4f951f487b96b1f2b5a2795cf8b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-editables/4caad070b55cf4f951f487b96b1f2b5a2795cf8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
