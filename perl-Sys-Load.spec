#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Sys
%define		pnam	Load
Summary:	Sys::Load - Perl module for getting the current system load and uptime
Summary(pl):	Sys::Load - modu³ Perla do odczytywania obci±¿enia systemu i uptime'u
Name:		perl-Sys-Load
Version:	0.2
Release:	5
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	370372db0ddbcde3725049157e0bc5ad
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getload() returns 3 elements: representing load averages over the last
1, 5 and 15 minutes.  uptime() returns the system uptime in seconds.

%description -l pl
getload() zwraca 3 warto¶ci, reprezentuj±ce ¶rednie obci±¿enie systemu
w ci±gu ostatnich 1, 5 i 15 minut. uptime() zwraca uptime systemu w
sekundach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorarch}/Sys/*.pm
%dir %{perl_vendorarch}/auto/Sys/Load
%attr(755,root,root) %{perl_vendorarch}/auto/Sys/Load/*.so
%{perl_vendorarch}/auto/Sys/Load/*.bs
%{_mandir}/man3/*
