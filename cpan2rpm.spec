Summary:	Create RPMS from CPAN modules
Name:		cpan2rpm
Version:	1.2
Release:	1
License:	GPL/Artistic
Group:          Development/Languages/Perl
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cpan2rpm creates RPMs from CPAN packages, automating the locating,
fetching, spec file creation and building of the package.

%prep
%setup -q -n %{name}-%{version}

%build
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
%{_libdir}/rpm/brp-compress
find $RPM_BUILD_ROOT/ -type f -print | sed "s@^$RPM_BUILD_ROOT@@g" > %{name}-filelist

%files -f %{name}-filelist
%defattr(644,root,root,755)
