%define	name	tuxkart
%define	version	0.4.0
%define release 	12

Summary:	Tuxedo T. Penguin stars in Tuxkart
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Games/Arcade
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}-mdkimgs.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-remove-O6.patch
Patch1:		%{name}-gownsbow-drv.patch
Patch2:		tuxkart-0.4.0-link.patch
URL:		http://tuxkart.sourceforge.net/
BuildRequires:	pkgconfig(x11)
BuildRequires:	mesaglu-devel
BuildRequires:	plib-devel

%description
This is another game that stars your Favorite Hero: Tux, the Linux Penguin.

%prep
%setup -q -D -a 1
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
autoreconf -fi
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Name=Tuxkart
Comment=Karting with tux
Icon=%{name}
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}
%{_datadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%doc README CHANGES ChangeLog NEWS


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.4.0-10mdv2011.0
+ Revision: 634739
- fix linkage

* Wed May 27 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4.0-9mdv2010.0
+ Revision: 380068
- fix license (GPLv2)

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-8mdv2009.0
+ Revision: 261706
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-7mdv2009.0
+ Revision: 254973
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Funda Wang <fwang@mandriva.org>
    - fix desktop entry (bug#37493)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.4.0-4mdv2008.1
+ Revision: 132310
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel


* Thu Nov 23 2006 Lenny Cartier <lenny@mandriva.com> 0.4.0-4mdv2007.0
+ Revision: 86607
- Mkrel
- Import tuxkart

