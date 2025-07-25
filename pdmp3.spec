Summary:	PDMP3 is a MP3 manager for GNOME
Summary(pl.UTF-8):	PDMP3 - zarządca MP3 dla GNOME
Name:		pdmp3
Version:	1.5.0
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	ftp://maul.viptx.net/pub/pdmp3/%{name}-%{version}.tar.gz
# Source0-md5:	05f1e189c4a5eed5ef82e8a9b76199d6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ac.patch
URL:		http://maul.viptx.net/software/pdmp3.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
Requires:	xmms
Requires:	gnapster
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
PDMP3 is a program to manage your MP3 collection. It supports id3 tag
editing, file rename and deletion, playlist creation and other little
utilities. It was written in C and uses GNOME and GTK+ as it's
graphical interface.

%description -l pl.UTF-8
PDMP3 jest programem do zarządzania zbiorem plików MP3. Obsługuje
edycję tagów id3, zmianę nazwy i usuwanie plików, tworzenie playlist i
inne małe narzędzia. Używa GNOME i GTK+ jako interfejsu graficznego.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
rm -f missing
%{__gettextize}
%{__autoconf}
%{__aclocal} -I macros
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Multimedia

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
