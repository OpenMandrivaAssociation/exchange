#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/exchange exchange; \
#cd exchange; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "exchange" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf exchange-$PKG_VERSION.tar.xz exchange/ --exclude .svn --exclude .*ignore

%define svnrev	54300

%define	major	0
%define	libname		%mklibname	%{name} %{major}
%define	develname	%mklibname	%{name} -d

Summary:	The enlightened way how to exchange stuff 
Name:		exchange
Version:	0.0.0.002
Release:	0.%{svnrev}.1
License:	GPLv2
Group:		System/Libraries
URL:		http://enlightenment.org/
Source0: 	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(libxml-2.0)

%description
The enlightened way how to exchange stuff

%package -n %{libname}
Summary:    Exchange library
Group:      System/Libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{develname}
Summary:    Exchange headers, libraries, documentation and test programs
Group:      Development/Other
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Headers and libraries from %{name}

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/exchange*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc

