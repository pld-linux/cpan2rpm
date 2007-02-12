#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Create RPMS from CPAN modules
Summary(pl.UTF-8):   Narzędzie tworzące pakiety RPM z modułów CPAN
Name:		cpan2rpm
Version:	2.028
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/E/EC/ECALDER/%{name}-%{version}.tar.gz
# Source0-md5:	4f85e07dfa848e5b72791aed975e8bc4
Patch0:		%{name}-make.patch
URL:		http://perl.arix.com/cpan2rpm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpan2rpm creates RPMs from CPAN packages, automating the locating,
fetching, spec file creation and building of the package.

%description -l pl.UTF-8
cpan2rpm tworzy pakiety RPM z pakietów CPAN, automatycznie je
znajdując, ściągając, tworząc plik spec i budując pakiet.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

# avoid running cpan2rpm and using network
touch cpan2rpm.spec

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
