# $Id: $

# Authority: dries

Summary: Screensaver with flames
Name: kflamesaver
Version: 0.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://kde-apps.org/content/show.php?content=4485

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel
%{?fc2:BuildRequires:libselinux-devel}

# Screenshot: http://kde-apps.org/content/pics/4485-1.png

%description
A screensaver for KDE with flame effects like in Twin Peaks.

%prep
%{__rm} -rf %{buildroot}
%setup

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
%{__make} install-strip DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/
mv %{buildroot}/usr/share/applnk/System/ScreenSavers/kflamesaver.desktop %{buildroot}/usr/share/apps/kscreensaver/ScreenSavers/

%files
%defattr(-,root,root, 0755)
%{_bindir}/kflamesaver.kss
%{_datadir}/apps/kscreensaver/ScreenSavers/kflamesaver.desktop
%{_datadir}/apps/kflamesaver/laura_and_coop.png

%changelog
* Sat Jan 10 2004 Dries Verachtert <dries@ulyssis.org> 0.1-1
- first packaging for Fedora Core 1
