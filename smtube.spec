Name:		smtube
Version:	14.8.0
Release:	1
Summary:	Allows to play and download videos from YouTube
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/SMTube/%{version}/%{name}-%{version}.tar.bz2
Patch0:		smtube-1.6-optflags.patch
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist

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
	QMAKE=%{qt4bin}/qmake \
	LRELEASE=%{qt4bin}/lrelease

%install
%makeinstall_std PREFIX=%{_prefix}

%files
%doc Changelog *.txt
%{_bindir}/%{name}
%{_datadir}/applications/smtube.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/translations/*
