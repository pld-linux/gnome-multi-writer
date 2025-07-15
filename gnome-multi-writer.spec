Summary:	Write an ISO file to multiple USB devices at once
Summary(pl.UTF-8):	Zapis pliku obrazu ISO na wiele urządzeń USB jednocześnie
Name:		gnome-multi-writer
Version:	3.32.1
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-multi-writer/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	6eba6f5c86d18abc5d3b4afeb879f543
URL:		https://wiki.gnome.org/Apps/MultiWriter
# appstream-util
BuildRequires:	appstream-glib
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.46.0
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gtk+3-devel >= 3.11.2
BuildRequires:	libcanberra-gtk3-devel >= 0.10
BuildRequires:	libgusb-devel >= 0.2.7
BuildRequires:	meson >= 0.46.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	udisks2-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.46.0
Requires:	glib2 >= 1:2.46.0
Requires:	gtk+3 >= 3.11.2
Requires:	libcanberra-gtk3 >= 0.10
Requires:	libgusb >= 0.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME MultiWriter can be used to write an ISO file to multiple USB
devices at once. Supported drive sizes are between 1GB and 32GB.

This application may be useful for QA testing, to create a GNOME Live
image for a code sprint or to create hundreds of LiveUSB drives for a
trade show.

%description -l pl.UTF-8
GNOME MultiWriter służy do zapisu pliku ISO na wiele urządzeń USB
jednocześnie. Obsługiwane są rozmiary urządzeń od 1GB do 32GB.

Ta aplikacja może być przydatna do testów, do tworzenia obrazu GNOME
Live na sprint kodowania lub do tworzenia setek pendrive'ów LiveUSB na
targi.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS README.md
%attr(755,root,root) %{_bindir}/gnome-multi-writer
%attr(755,root,root) %{_libexecdir}/gnome-multi-writer-probe
%{_datadir}/glib-2.0/schemas/org.gnome.MultiWriter.gschema.xml
%{_datadir}/polkit-1/actions/org.gnome.MultiWriter.policy
%{_datadir}/metainfo/org.gnome.MultiWriter.appdata.xml
%{_desktopdir}/org.gnome.MultiWriter.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.MultiWriter.png
%{_mandir}/man1/gnome-multi-writer.1*
