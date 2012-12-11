Name:		smtube
Version:	1.1
Release:	%mkrel 1
Summary:	Allows to play and download videos from YouTube
License:	GPLv2+
Group:		Video
Url:		http://smplayer.sourceforge.net
Source0:	http://downloads.sourceforge.net/smplayer/SMTube/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist

%description
SMTube is a tool for searching and downloading videos from YouTube.
It supports SMPlayer, VLC and some other players.

%prep
%setup -q

%build
%setup_compile_flags
%make PREFIX=%{_prefix} QMAKE=%{qt4bin}/qmake LRELEASE=%{qt4bin}/lrelease

%install
%__rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

%clean
%__rm -rf %{buildroot}

%files
%doc Changelog *.txt
%{_bindir}/%{name}
%{_datadir}/applications/smtube.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/translations/*



%changelog
* Wed Apr 04 2012 Andrey Bondrov <abondrov@mandriva.org> 1.1-1mdv2011.0
+ Revision: 789125
- imported package smtube

