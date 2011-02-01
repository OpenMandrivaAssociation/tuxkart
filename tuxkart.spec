%define	name	tuxkart
%define	version	0.4.0
%define	release	%mkrel 10

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
BuildRequires:	libx11-devel
BuildRequires:	mesaglu-devel
BuildRequires:	plib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
