%define	major 1
%define libname	%mklibname ooh323c %{major}

Summary:	Objective Systems Open H.323 library
Name:		ooh323c
Version:	0.8.2
Release:	6
Group:		System/Libraries
License:	GPL
URL:		https://www.obj-sys.com/open/
Source0:	http://switch.dl.sourceforge.net/sourceforge/ooh323c/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool

%description
Objective Systems Open H.323 for C is a simple H.323 protocol stack. It
contains signaling logic to allow H.323 channels to be created and terminated.
The code is developed in C to allow easy portability to different platform
types (including embedded).

%package -n	%{libname}
Summary:	Objective Systems Open H.323 library
Group:          System/Libraries

%description -n	%{libname}
Objective Systems Open H.323 for C is a simple H.323 protocol stack. It
contains signaling logic to allow H.323 channels to be created and terminated.
The code is developed in C to allow easy portability to different platform
types (including embedded).

%package -n	%{libname}-devel
Summary:	Static library and header files for the ooh323c library
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
Objective Systems Open H.323 for C is a simple H.323 protocol stack. It
contains signaling logic to allow H.323 channels to be created and terminated.
The code is developed in C to allow easy portability to different platform
types (including embedded).

This package contains the static ooh323c library and its header files.

%prep
%setup -q

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build
%configure2_5x

%make

%install
%makeinstall_std

%files -n %{libname}
%doc COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%doc doc/*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.8.2-4mdv2010.0
+ Revision: 430204
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.2-3mdv2009.0
+ Revision: 254542
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8.2-1mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Dec 18 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2007.0
+ Revision: 98557
- Import ooh323c

* Mon Dec 18 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2007.1
- initial Mandriva package

