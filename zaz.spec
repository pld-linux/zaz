Summary:	An arcade action puzzle game
Summary(pl.UTF-8):	Zręcznościowa gra logiczna
Name:		zaz
Version:	0.2.9
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/zaz/%{name}-%{version}.tar.gz
# Source0-md5:	74dca44e4d1d9956d551f17759e80a38
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-usless_files.patch
URL:		http://zaz.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ftgl-devel
BuildRequires:	libdrm-devel
BuildRequires:	libogg-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zaz is an arcade action puzzle game where the objective is to get rid
of all incoming balls by rearranging their order. Currently it
includes 6 different levels.

%description -l pl.UTF-8
Zaz to zręcznościowa gra logiczna, w której celem jet pozbycie się
wszystkich kul zmieniając ich ustawienie. Aktualnie gra zawiera 6
różnych poziomów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# inexistent files
%{__sed} -i '/mus5.ogg/d' data/Makefile.am
%{__sed} -i '/levels.list/d' data/Makefile.am

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
