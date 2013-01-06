Name:		elementary-gtk
Version:	3.1
Release:	1%{?dist}
Summary:	Elementary GTK theme

Group:		User Interface/Desktops
License:	GPLv2+
BuildArch:	noarch
URL:		http://danrabbit.deviantart.com/art/elementary-gtk-theme-83104033	
Source0:	http://www.deviantart.com/download/83104033/elementary_gtk_theme_by_danrabbit-d1dh7hd.zip
#Patch0:		%{name}.patch

BuildRequires:	gtk2-devel
Requires:	gtk-murrine-engine

%description
This package contains the Elementary GTK Theme for the GNOME desktop.

%prep
%setup -q
#%patch0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes/elementary
cp -a %{_builddir}/%{name}-%{version}/* %{buildroot}%{_datadir}/themes/elementary/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/themes/elementary/

%changelog
* Mon May 21 2012 Chris Smart <chris@kororaa.org> 3.1-1
- Update to upstream 3.1 release.

* Mon Mar 14 2011 Chris Smart <chris@kororaa.org> 2.1-1
- Initial port from oxygen-gtk.spec.

