#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	Load
Summary:	Sys::Load - Perl module for getting the current system load and uptime
#Summary(pl):	
Name:		perl-Sys-Load
Version:	0.2
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getload() returns 3 elements: representing load averages over the last 1,
5 and 15 minutes.  uptime() returns the system uptime in seconds.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitearch}/%{pdir}/*.pm
%dir %{perl_sitearch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_sitearch}/auto/%{pdir}/%{pnam}/*.so
%{perl_sitearch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
