# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-LZF

Summary: POE filter wrapped around Compress::LZF
Name: perl-POE-Filter-LZF
Version: 1.63
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-LZF/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-LZF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
A POE filter wrapped around Compress::LZF.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/POE::Filter::LZF.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
#%{perl_vendorlib}/POE/Filter/LZF/
%{perl_vendorlib}/POE/Filter/LZF.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.63-1
- Updated to release 1.63.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
