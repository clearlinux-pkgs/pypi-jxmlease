#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jxmlease
Version  : 1.0.3
Release  : 11
URL      : https://files.pythonhosted.org/packages/8d/6a/b2944628e019c753894552c1499bf60e2cef9efea138756c5d66f0d5eb98/jxmlease-1.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/6a/b2944628e019c753894552c1499bf60e2cef9efea138756c5d66f0d5eb98/jxmlease-1.0.3.tar.gz
Summary  : jxmlease converts between XML and intelligent Python data structures.
Group    : Development/Tools
License  : MIT
Requires: pypi-jxmlease-license = %{version}-%{release}
Requires: pypi-jxmlease-python = %{version}-%{release}
Requires: pypi-jxmlease-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
jxmlease
========
Welcome to jxmlease: a Python module for converting XML to
intelligent Python data structures, and converting Python data
structures to XML.

%package license
Summary: license components for the pypi-jxmlease package.
Group: Default

%description license
license components for the pypi-jxmlease package.


%package python
Summary: python components for the pypi-jxmlease package.
Group: Default
Requires: pypi-jxmlease-python3 = %{version}-%{release}

%description python
python components for the pypi-jxmlease package.


%package python3
Summary: python3 components for the pypi-jxmlease package.
Group: Default
Requires: python3-core
Provides: pypi(jxmlease)

%description python3
python3 components for the pypi-jxmlease package.


%prep
%setup -q -n jxmlease-1.0.3
cd %{_builddir}/jxmlease-1.0.3
pushd ..
cp -a jxmlease-1.0.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656396364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jxmlease
cp %{_builddir}/jxmlease-1.0.3/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jxmlease/ab0ac8ffb1233c8a2311dbfdae920b69f7d4f497
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jxmlease/ab0ac8ffb1233c8a2311dbfdae920b69f7d4f497

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
