Name:		plasmate
Summary:	KDE Plasma Add-On Creator
Version:	1.0
Release:	2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://projects.kde.org/projects/extragear/sdk/plasmate
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/src/%{name}-%{version}.tar.gz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	git-core
Requires:	git-core
Conflicts:	kdebase4-workspace < 2:4.9.90

%description
A small IDE taylored for development of Plasma components, such as Widgets,
Runners, Dataengines.

%files
%{_kde_bindir}/kwin-windowswitcherpreviewer
%{_kde_bindir}/plasma-remote-widgets-browser
%{_kde_bindir}/plasmaengineexplorer
%{_kde_bindir}/plasmakconfigxteditor
%{_kde_bindir}/plasmaremoteinstaller
%{_kde_bindir}/plasmate
%{_kde_bindir}/plasmawallpaperviewer
%{_kde_bindir}/plasmoidviewer
%{_kde_libdir}/kde4/plasma_containment_studiopreviewer.so
%{_kde_applicationsdir}/plasmate.desktop
%{_kde_appsdir}/%{name}
%{_kde_configdir}/plasmate.knsrc
%{_kde_services}/plasma-containment-studiopreviewer.desktop
%{_kde_mandir}/man1/plasmaengineexplorer.1.*
%{_kde_mandir}/man1/plasmoidviewer.1.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
rm -f %{buildroot}/%{_kde_iconsdir}/hicolor/*/apps/plasmagik.png

