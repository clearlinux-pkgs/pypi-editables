#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-editables
Version  : 0.3
Release  : 2
URL      : https://files.pythonhosted.org/packages/01/b0/a2a87db4b6cb8e7d57004b6836faa634e0747e3e39ded126cdbe5a33ba36/editables-0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/b0/a2a87db4b6cb8e7d57004b6836faa634e0747e3e39ded126cdbe5a33ba36/editables-0.3.tar.gz
Summary  : Editable installations
Group    : Development/Tools
License  : MIT
Requires: pypi-editables-license = %{version}-%{release}
Requires: pypi-editables-python = %{version}-%{release}
Requires: pypi-editables-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

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
%setup -q -n editables-0.3
cd %{_builddir}/editables-0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649741258
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-editables
cp %{_builddir}/editables-0.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-editables/4caad070b55cf4f951f487b96b1f2b5a2795cf8b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
