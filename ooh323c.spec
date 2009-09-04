%define	major 1
%define libname	%mklibname ooh323c %{major}

Summary:	Objective Systems Open H.323 library
Name:		ooh323c
Version:	0.8.2
Release:	%mkrel 4
Group:		System/Libraries
License:	GPL
URL:		http://www.obj-sys.com/open/
Source0:	http://switch.dl.sourceforge.net/sourceforge/ooh323c/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
Objective Systems Open H.323 for C is a simple H.323 protocol stack. It
contains signaling logic to allow H.323 channels to be created and terminated.
The code is developed in C to allow easy portability to different platform
types (including embedded).

This package contains the static ooh323c library and its header files.

%prep

%setup -q -n %{name}-%{version}

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc/*
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


