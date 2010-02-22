Summary:	An arcade action puzzle game
Summary(pl.UTF-8):	Zręcznościowa gra logiczna
Name:		zaz
Version:	0.3.3
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/zaz/%{name}-%{version}.tar.gz
# Source0-md5:	a538fe87780a56b47bc9b792ff6ae388
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-usless_files.patch
URL:		http://zaz.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ftgl-devel >= 2.1.3
BuildRequires:	gettext-devel
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
includes 7 different levels.

%description -l pl.UTF-8
Zaz to zręcznościowa gra logiczna, w której celem jet pozbycie się
wszystkich kul zmieniając ich ustawienie. Aktualnie gra zawiera 7
różnych poziomów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/zaz
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
