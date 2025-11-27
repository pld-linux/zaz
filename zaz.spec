Summary:	An arcade action puzzle game
Summary(hu.UTF-8):	Akció-kirakó játék
Summary(pl.UTF-8):	Zręcznościowa gra logiczna
Name:		zaz
Version:	1.0.1
Release:	2
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://downloads.sourceforge.net/zaz/%{name}-%{version}.tar.gz
# Source0-md5:	987804f7b2ecdd7847d21e1ccf45c210
Source1:	%{name}-docs.tar.gz
# Source1-md5:	c1d35b69edf80bab01262ca272405181
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-usless_files.patch
URL:		https://zaz.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	gettext-tools
BuildRequires:	libdrm-devel
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zaz is an arcade action puzzle game where the objective is to get rid
of all incoming balls by rearranging their order. Currently it
includes 23 different levels.

%description  -l hu.UTF-8
Zaz egy akció kirakó játék, amelyben a cél, hogy az összes bejövő
labdától megszabadulj úgy, hogy őket sorbarendezd. Jelenleg 23
különböző pálya van.

%description -l pl.UTF-8
Zaz to zręcznościowa gra logiczna, w której celem jet pozbycie się
wszystkich kul zmieniając ich ustawienie. Aktualnie gra zawiera 23
różnych poziomów.

%prep
%setup -q -a 1
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal} -Im4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-icondir="%{_pixmapsdir}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog docs/*
%attr(755,root,root) %{_bindir}/zaz
%{_datadir}/%{name}
%{_desktopdir}/zaz.desktop
%{_pixmapsdir}/zaz.xpm
