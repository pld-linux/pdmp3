Summary:	PDMP3 is a mp3 manager for gnome
Name:		pdmp3
Version:	1.5.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://maul.viptx.net/pub/pdmp3/%{name}-%{version}.tar.gz
Patch0:		pdmp3-DESTDIR.patch
URL:		http://maul.viptx.net/software/pdmp3.html
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
Requires:	xmms
Requires:	gnapster
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
PDMP3 is a program to manage your mp3 collection. It supports id3 tag
editing, file rename and deletion, playlist creation and other little
utilities. It was written in C and uses gnome and gtk as it's graphical
interface.

%prep
%setup -q
%patch0 -p1

%build
automake
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Multimedia

gzip -9nf AUTHORS ChangeLog NEWS README

#%find_lang %{name}

%clean                                                                          
rm -rf $RPM_BUILD_ROOT                                                          
                                                                                
%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/*
%{_pixmapsdir}/*
