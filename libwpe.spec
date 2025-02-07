%define major 1
%define libname %mklibname wpe
%define oldlibname %mklibname wpe 1
%define devname %mklibname wpe -d


Name:           libwpe
Version:        1.16.2
Release:        1
Summary:        General-purpose library for the WPE-flavored port of WebKit
Group:		System/Libraries
License:        BSD
URL:            https://github.com/WebPlatformForEmbedded/%{name}
Source0:        https://github.com/WebPlatformForEmbedded/libwpe/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  mesa-common-devel
BuildRequires:  pkgconfig(xkbcommon)

Provides: wpebackend = %{EVRD}
Obsoletes: wpebackend < 0.2.0-2

%description
General-purpose library developed for the WPE-flavored port of WebKit

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
License:	LGPLv2+
%rename %{oldlibname}

%description -n %{libname}
Libraries for %{name}.

%files -n %{libname}
%license COPYING
%doc NEWS
%{_libdir}/libwpe-1.0.so.%{major}*

####################################################################

%package -n    %{devname}
Summary:       Development files for %{name}
Requires:      %{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.


%files -n %{devname}
%{_includedir}/wpe-1.0/
%{_libdir}/libwpe-1.0.so
%{_libdir}/pkgconfig/wpe-1.0.pc

####################################################################

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%make_build

%install
%make_install -C build
