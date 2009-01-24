#
# TODO:	BRs
#	separate package for libgstreamer_playbin.so
#
%include	/usr/lib/rpm/macros.mono
Summary:	A subtitle editor for the GNOME desktop
Summary(pl.UTF-8):	Edytor napisów dla środowiska GNOME
Name:		gnome-subtitles
Version:	0.8
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gnome-subtitles/%{name}-%{version}.tar.gz
# Source0-md5:	9590389ba91f9cfd94b6b36454dc2420
URL:		http://gnome-subtitles.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.7
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sublib-devel >= 0.9
Requires:	enchant
Requires:	dotnet-gnome-sharp >= 2.16
Requires:	dotnet-gtk-sharp2 >= 2.12.7
Requires:	gtkspell
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

%build
cd gstreamer-playbin-0.2.1
%{__libtoolize}
%{__autoconf}
cd ..
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{find_lang} %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) /etc/gconf/schemas/%{name}.schemas
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.dll*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%attr(755,root,root) %{_libdir}/%{name}/libgstreamer_playbin.so
%{_libdir}/%{name}/*.exe.config
%{_mandir}/man1/*.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
