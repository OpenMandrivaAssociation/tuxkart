%define	name	tuxkart
%define	version	0.4.0
%define	release	%mkrel 5

Summary:	Tuxedo T. Penguin stars in Tuxkart
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}-mdkimgs.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-remove-O6.patch
Patch1:		%{name}-gownsbow-drv.patch
URL:		http://tuxkart.sourceforge.net/
BuildRequires:	plib Mesa-common-devel MesaGLU-devel X11-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is another game that stars your Favorite Hero: Tux, the Linux Penguin.

%prep
%setup -q -D -a 1
%patch0 -p0
%patch1 -p0

%build
%configure --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} bindir=$RPM_BUILD_ROOT%{_gamesbindir}

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

%post
%{update_menus}
 
%postun
%{clean_menus} 

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
