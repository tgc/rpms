# $Id$
# Authority: dries
# Upstream: A. Schiffler <aschiffler$appwares,com>
# Screenshot: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/Screenshots/SDL_gfxPrimitives.jpg
# ScreenshotURL: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html

Summary: Graphic primitives, rotozoomer, framerate control and image filters
Name: SDL_gfx
Version: 2.0.12
Release: 3
License: LGPL
Group: System Environment/Libraries
URL: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/index.html
Source: http://www.ferzkopp.net/~aschiffler/Software/SDL_gfx-2.0/SDL_gfx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, gcc-c++, automake, autoconf, perl

%description
The SDL_gfx library offers several components: Graphic Primitives,
Rotozoomer, Framerate control, and MMX image filters. The Primitives
component provides basic drawing routines: pixels, hlines, vlines, lines,
aa-lines, rectangles, circles, ellipses, trigons, polygons, Bezier curves,
and an 8x8 pixmap font for drawing onto any SDL Surface. Full alpha
blending, hardware surface locking, and all surface depths are supported.
The Rotozoomer can use interpolation for high quality output.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%ifnarch %{ix86}
    --disable-mmx
%endif
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc NEWS LICENSE README AUTHORS COPYING
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/SDL/*.h
%exclude %{_libdir}/*.la

%changelog
* Thu Nov 11 2004 Matthias Saou <http://freshrpms.net/> 2.0.12-3
- Explicitly disable mmx for non-ix86 to fix build on x86_64.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-3
- fixed some buildrequirements so the correct version of libSDL_gfx.so 
  can be found in the list of provides.

* Fri Oct 22 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-2
- rebuild

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 2.0.12-1
- Update to version 2.0.12.

* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 2.0.10-1
- Initial package

