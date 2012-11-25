Name:           libical
BuildRequires:  db4-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-devel
Url:            http://sourceforge.net/projects/freeassociation/
Version:        0.48
Release:        0
Summary:        An Implementation of Basic iCAL Protocols
License:        MPL-1.1 or LGPL-2.1
Group:          Development/Libraries/C and C++
Source:         libical-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libical is an open source implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package devel
Summary:        An implementation of basic iCAL protocols
Group:          Development/Libraries/C and C++
Requires:       libical = %{version}

%description devel
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols. (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%package doc
Summary:        An Implementation of Basic iCAL Protocols
Group:          Development/Libraries/C and C++
Requires:       libical = %{version}

%description doc
Libical is an open source implementation of the IETF's iCalendar
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It
parses iCal components and provides a C API for manipulating the
component properties, parameters, and subcomponents.

%prep
%setup -q

%build
# triger autoreconf since the 0.46 tarball is missing autotools bootstrap files
autoreconf -f -i
%{configure} \
	--with-bdb4 \
	--with-bdb4-dir=%{_prefix} \
	--without-builtintz \
	--enable-shared \
	--disable-static
%{__make} %{?_smp_mflags}

%install
%{makeinstall}
%{__rm} $RPM_BUILD_ROOT/%{_libdir}/libical*.la
%{__rm} doc/Makefile*
%{__rm} -rf examples/.deps
%{__rm} -rf examples/.libs
%{__rm} examples/*.o
%{__rm} examples/doesnothing
%{__rm} scripts/Makefile*
%{__sed} -i -e '1s,.*,#!/usr/bin/perl,' scripts/mkneticali.pl

%post  -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/libical.pc
%{_includedir}/ical.h
%{_includedir}/libical

%files doc
%defattr(-,root,root)
%doc doc examples scripts

%changelog
