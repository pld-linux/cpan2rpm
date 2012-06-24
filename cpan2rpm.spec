Summary:	Create RPMS from CPAN modules
Summary(pl):	Narz�dzie tworz�ce pakiety RPM z modu��w CPAN
Name:		cpan2rpm
Version:	1.2
Release:	1
License:	GPL/Artistic
Group:          Development/Languages/Perl
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	70cc987bc884aa911dcf3bea7596f42e
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpan2rpm creates RPMs from CPAN packages, automating the locating,
fetching, spec file creation and building of the package.

%description -l pl
cpan2rpm tworzy pakiety RPM z pakiet�w CPAN, automatycznie je
znajduj�c, �ci�gaj�c, tworz�c plik spec i buduj�c pakiet.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
