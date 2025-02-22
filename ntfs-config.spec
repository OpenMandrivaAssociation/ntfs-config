%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

Summary:	GUI tool to enable/disable write support for NTFS device
Name:		ntfs-config
Version:	1.1
Release:	10
License: 	GPL
Group:  	Graphical desktop/GNOME
Url:		https://flomertens.free.fr/ntfs-config/
Source0:	%{name}-%{version}.tar.gz
Patch0:		ntfs-config-1.1-desktop.patch
BuildRequires:  desktop-file-utils
BuildRequires:	intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  usermode
BuildRequires:  pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python2)
Requires:	gksu
Requires:	ntfs-3g
Requires:	pygtk2.0-libglade
Requires:       usermode

%description
This program will allow you to easily configure all of your NTFS devices to
allow write support.  For that use, it will configure them to use the ntfs-3g
driver. You'll also be able to easily disable this feature.

For more information about ntfs-3g : http://www.ntfs-3g.org

%prep
%setup -q
%autopatch -p1

#fix ru
rm -f po/ru.mo
autoconf

%build
export PYTHON=%__python2
%configure
%make

%install
%makeinstall_std

#For compartibles without HAL
mkdir -p %{buildroot}%{_sysconfdir}/hal/fdi/policy
echo "This directory need for ntfs-config. Not remove!" > %{buildroot}%{_sysconfdir}/hal/fdi/policy/README

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sbindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/*
%{_mandir}/man8/*
%{py2_platsitedir}/NtfsConfig
%{_sysconfdir}/hal/fdi/policy/README

