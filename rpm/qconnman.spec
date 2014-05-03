# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       qconnman

# >> macros
# << macros

Summary:    Qt wrapper for ConnMan
Version:    1.21.0
Release:    1
Group:      System/Libraries
License:    LGPL-2.1+
URL:        https://bitbucket.org/devonit/qconnman
Source0:    %{name}-%{version}.tar.xz
Source100:  qconnman.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  gcc-c++
BuildRequires:  dbus
BuildRequires:  connman

%description
Qt wrapper for ConnMan.

%package devel
Summary:    Development files for qconnman
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications |
using qconnman.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS README
%{_libdir}/*.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
# >> files devel
# << files devel
