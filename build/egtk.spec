%global	short_name	eGTK
%global	full_name	elementary GTK

Name:		egtk
Version:	3.1
Release:	2%{?dist}
Summary:	The %{short_name} (%{full_name}) themes for GTK+2, GTK+3, Metacity and Xfwm4

Group:		User Interface/Desktops
License:	GPLv2
URL:		https://launchpad.net/%{name}
Source0:	https://launchpad.net/%{name}/3.x/%{version}/+download/elementary.tar.gz

BuildArch:	noarch	

%description
The official %{full_name} theme designed to be smooth, attractive, fast, and 
usable.


%package common
Summary:	Files common to %{short_name} themes
Group:		User Interface/Desktops

%description common
Files which are common to all %{short_name} (%full_name) themes.


%package gtk2-theme
Summary:	The %{short_name} theme for GTK+2
Group:		User Interface/Desktops
Requires:	%{name}-common = %{version}-%{release}, gtk-murrine-engine
Obsoletes: elementary-gtk

%description gtk2-theme
Theme for GTK+2 as part of the %{short_name} (%full_name) theme.


%package gtk3-theme
Summary:	The %{short_name} theme for GTK+3
Group:		User Interface/Desktops
Requires:	%{name}-common = %{version}-%{release}, gtk-unico-engine
Provides: elementary-gtk
Obsoletes: elementary-gtk

%description gtk3-theme
Theme for GTK+3 as part of the %{short_name} (%full_name) theme.


%package metacity-theme
Summary:	The %{short_name} theme for Metacity
Group:		User Interface/Desktops
Requires:	%{name}-common = %{version}-%{release}, metacity
Obsoletes: elementary-gtk

%description metacity-theme
Theme for Metacity as part of the %{short_name} (%full_name) theme.


%package xfwm4-theme
Summary:	The %{short_name} theme for Xfwm4
Group:		User Interface/Desktops
Requires:	%{name}-common = %{version}-%{release}, xfwm4
Obsoletes: elementary-gtk

%description xfwm4-theme
Theme for Xfwm4 as part of the %{short_name} (%full_name) theme.


%prep
%setup -q -c
# Remove backup files
find . -name '*~' -type f -exec rm -f '{}' \;
# Remove Bazaar-related files
rm -rf .bzr
# Remove "index.theme"
rm -f index.theme


%build
# Nothing to build


%install
for dir in gtk-2.0 gtk-3.0 metacity-1 xfwm4
do
	mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{short_name}/$dir
	cp -pr ./*/$dir/* %{buildroot}%{_datadir}/themes/%{short_name}/$dir
done


%files common
%doc ./*/AUTHORS ./*/CONTRIBUTORS ./*/COPYING
%dir %{_datadir}/themes/%{short_name}/


%files gtk2-theme
%dir %{_datadir}/themes/%{short_name}/gtk-2.0/
%{_datadir}/themes/%{short_name}/gtk-2.0/*


%files gtk3-theme
%dir %{_datadir}/themes/%{short_name}/gtk-3.0/
%{_datadir}/themes/%{short_name}/gtk-3.0/*


%files metacity-theme
%dir %{_datadir}/themes/%{short_name}/metacity-1/
%{_datadir}/themes/%{short_name}/metacity-1/*


%files xfwm4-theme
%dir %{_datadir}/themes/%{short_name}/xfwm4/
%{_datadir}/themes/%{short_name}/xfwm4/*


%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Mattia Meneguzzo <odysseus@fedoraproject.org> - 3.1-1
- Initial package for Fedora
