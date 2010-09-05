Summary:	An arcade action puzzle game
Summary(hu.UTF-8):	Akció-kirakó játék
Summary(pl.UTF-8):	Zręcznościowa gra logiczna
Name:		zaz
Version:	1.0.0
Release:	2
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/zaz/%{name}-%{version}.tar.bz2
# Source0-md5:	d92a043780d06c699da0ba04aab32a6b
Source1:	bonus1.png
Source2:	bonus2.png
Source3:	bonus3.png
Source4:	bonus4.png
Source5:	bonus5.png
Source6:	logo.png
Source7:	doc.html
Source8:	screen_mini.jpg
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

install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install AUTHORS ChangeLog \
	%{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/zaz
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
