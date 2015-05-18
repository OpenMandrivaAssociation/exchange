%define git	20150518

%define	major	0
%define	libname		%mklibname	%{name} %{major}
%define	develname	%mklibname	%{name} -d

Summary:	The enlightened way how to exchange stuff 
Name:		exchange
Version:	0.0.0.002
Release:	0.%{git}.1
License:	GPLv2
Group:		System/Libraries
URL:		https://git.enlightenment.org/website
Source0: 	%{name}-%{version}.%{git}.tar.xz

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

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/exchange*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*pc



%changelog
* Wed Jan 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.0.002-0.54300.1
+ Revision: 759649
- remove unneeded find_lang
- fixed main group
- imported package exchange


* Tue Jan 10 2012 Matthew Dawkins <mdawkins@unity-linux.org> 0.0.0.002-0.54300.1-unity2011
- new version 0.0.0.002

* Wed Aug 24 2011 Gianvacca <gianvacca@unity-linux.org> 0.0.0.002.54300-0.20110824.1-unity2011
- new snapshot

* Sat Mar 05 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110305.1-unity2011
- new snapshot 20110305

* Fri Jan 14 2011 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20110114.1-unity2011
- new snapshot 20110114

* Fri Dec 17 2010 OnlyHuman <halo.3.0sdt@googlemail.com> 0.0.1-0.20101203.1-unity2010
- new snapshot 20101203

* Tue Oct 12 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20101006.1-unity2010
- new snapshot 20101006

* Wed Aug 25 2010 mdawkins <mattydaw@gmail.com> 0.0.1-0.20100825.1-unity2010
- first build
