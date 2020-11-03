#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libndp
Version  : 1.7
Release  : 10
URL      : https://github.com/jpirko/libndp/archive/v1.7.tar.gz
Source0  : https://github.com/jpirko/libndp/archive/v1.7.tar.gz
Summary  : Neighbour discovery library.
Group    : Development/Tools
License  : LGPL-2.1
Requires: libndp-bin = %{version}-%{release}
Requires: libndp-lib = %{version}-%{release}
Requires: libndp-license = %{version}-%{release}
Requires: libndp-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
# libndp - Library for Neighbor Discovery Protocol #
This package contains a library which provides a wrapper
for IPv6 Neighbor Discovery Protocol.  It also provides a tool
named ndptool for sending and receiving NDP messages.

%package bin
Summary: bin components for the libndp package.
Group: Binaries
Requires: libndp-license = %{version}-%{release}

%description bin
bin components for the libndp package.


%package dev
Summary: dev components for the libndp package.
Group: Development
Requires: libndp-lib = %{version}-%{release}
Requires: libndp-bin = %{version}-%{release}
Provides: libndp-devel = %{version}-%{release}
Requires: libndp = %{version}-%{release}

%description dev
dev components for the libndp package.


%package dev32
Summary: dev32 components for the libndp package.
Group: Default
Requires: libndp-lib32 = %{version}-%{release}
Requires: libndp-bin = %{version}-%{release}
Requires: libndp-dev = %{version}-%{release}

%description dev32
dev32 components for the libndp package.


%package lib
Summary: lib components for the libndp package.
Group: Libraries
Requires: libndp-license = %{version}-%{release}

%description lib
lib components for the libndp package.


%package lib32
Summary: lib32 components for the libndp package.
Group: Default
Requires: libndp-license = %{version}-%{release}

%description lib32
lib32 components for the libndp package.


%package license
Summary: license components for the libndp package.
Group: Default

%description license
license components for the libndp package.


%package man
Summary: man components for the libndp package.
Group: Default

%description man
man components for the libndp package.


%prep
%setup -q -n libndp-1.7
cd %{_builddir}/libndp-1.7
pushd ..
cp -a libndp-1.7 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604442509
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604442509
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libndp
cp %{_builddir}/libndp-1.7/COPYING %{buildroot}/usr/share/package-licenses/libndp/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndptool

%files dev
%defattr(-,root,root,-)
/usr/include/ndp.h
/usr/lib64/libndp.so
/usr/lib64/pkgconfig/libndp.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libndp.so
/usr/lib32/pkgconfig/32libndp.pc
/usr/lib32/pkgconfig/libndp.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libndp.so.0
/usr/lib64/libndp.so.0.1.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libndp.so.0
/usr/lib32/libndp.so.0.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libndp/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/ndptool.8
