Name:		smtube
Version:	18.3.0
Release:	1
Summary:	Allows to play and download videos from YouTube
License:	GPLv2+
Group:		Video
Url:		https://www.smtube.org/
Source0:	http://sourceforge.net/projects/%{name}/files/SMTube/%{version}/%{name}-%{version}.tar.bz2
Patch0:		smtube-1.6-optflags.patch
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	pkgconfig(Qt5WebKitWidgets) 
BuildRequires:	pkgconfig(Qt5Widgets) 
BuildRequires:	pkgconfig(Qt5WebKit) 
BuildRequires:	pkgconfig(Qt5Gui) 
BuildRequires:	pkgconfig(Qt5Network) 
BuildRequires:	pkgconfig(Qt5Script) 
BuildRequires:	pkgconfig(Qt5Core)

Suggests:	smplayer

%description
SMTube is a tool for searching and downloading videos from YouTube.
It supports SMPlayer, VLC and some other players.

%prep
%setup -q
%patch0 -p1

%build
%setup_compile_flags
%make \
	PREFIX=%{_prefix} \
	QMAKE=%{_bindir}/qmake-qt5 \
	LRELEASE=%{_libdir}/qt5/bin/lrelease

%install
%makeinstall_std PREFIX=%{_prefix}

%files
%doc Changelog *.txt
%{_bindir}/%{name}
%{_datadir}/applications/smtube.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/translations/*
