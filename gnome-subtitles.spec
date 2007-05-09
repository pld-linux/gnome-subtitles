#
# TODO:	BRs
#
Summary:	A subtitle editor for the GNOME desktop
Summary(pl.UTF-8):	Edytor napisów dla środowiska GNOME
Name:		gnome-subtitles
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-subtitles/%{name}-%{version}.tar.gz
# Source0-md5:	5ae670478a278e83daf900a73dd906c9
Patch0:		%{name}-sh_wrapper.patch
URL:		http://gnome-subtitles.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Subtitles is a subtitle editor for the GNOME desktop. It
supports the most common text-based subtitle formats and allows for
subtitle editing, conversion and synchronization.

%description -l pl.UTF-8
Gnome Subtitles to edytor napisów dla środowiska GNOME. Obsługuje
większość popularnych tekstowych formatów napisów i umożliwia
modyfikowanie, konwersję i synchronizację napisów.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%config(noreplace) %verify(not md5 mtime size) /etc/gconf/schemas/%{name}.schemas
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.dll*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_mandir}/man1/*.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
