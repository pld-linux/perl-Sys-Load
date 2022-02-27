#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Sys
%define		pnam	Load
Summary:	Sys::Load - Perl module for getting the current system load and uptime
Summary(pl.UTF-8):	Sys::Load - moduł Perla do odczytywania obciążenia systemu i uptime'u
Name:		perl-Sys-Load
Version:	0.2
Release:	19
# sae as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	370372db0ddbcde3725049157e0bc5ad
URL:		http://search.cpan.org/dist/Sys-Load/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getload() returns 3 elements: representing load averages over the last
1, 5 and 15 minutes.  uptime() returns the system uptime in seconds.

%description -l pl.UTF-8
getload() zwraca 3 wartości, reprezentujące średnie obciążenie systemu
w ciągu ostatnich 1, 5 i 15 minut. uptime() zwraca uptime systemu w
sekundach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorarch}/Sys/*.pm
%dir %{perl_vendorarch}/auto/Sys/Load
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Load/*.so
%{_mandir}/man3/*
