Summary:	Enable/disable write support for internal and/or external NTFS device via a friendly gui
Name:		ntfs-config
Version:	1.0.1
Release:	%mkrel 1
License: 	GPL
Group:  	Graphical desktop/GNOME
Source0:	http://flomertens.free.fr/ntfs-config/download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://flomertens.free.fr/ntfs-config/
BuildRequires:  pygtk2.0-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-XML-Parser
BuildRequires:  usermode
Requires:	ntfs-3g
Requires:       gksu
Requires:	pygtk2.0-libglade
Requires:       usermode
%description
This program will allow you to easily configure all of your NTFS devices to allow write support.
For that use, it will configure them to use the ntfs-3g
driver. You'll also be able to easily disable this feature.

For more information about ntfs-3g : http://www.ntfs-3g.org

%prep
%setup -q

%build

%configure

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Configuration-Hardware" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%post
%update_menus

%postun
%clean_menus



%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %_sysconfdir/pam.d/ntfs-config-root
%config(noreplace) %_sysconfdir/security/console.apps/ntfs-config-root
%{_bindir}/%{name}
%_sbindir/ntfs-config-root
%{_datadir}/applications/*.desktop
%{_mandir}/man8/*
%{_datadir}/%{name}/*
%py_platsitedir/NtfsConfig


