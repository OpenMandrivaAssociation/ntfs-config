Summary:	Enable/disable write support for internal and/or external NTFS device via a friendly gui
Name:		ntfs-config
Version:	0.5.5
Release:	%mkrel 2
License: 	GPL
Group:  	Graphical desktop/GNOME
Source0:	http://flomertens.free.fr/ntfs-config/download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://flomertens.free.fr/ntfs-config/
BuildRequires:  gtk2-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  hal-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-XML-Parser
Requires:	ntfs-3g
Requires:	gksu

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
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man8/%{name}.8.bz2
%{_datadir}/%{name}/*



