#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Table
Summary:	HTML::Table perl module - producing HTML tables
Summary(pl.UTF-8):	Moduł perla HTML::Table - tworzenie tabelek w HTML-u
Name:		perl-HTML-Table
Version:	2.08a
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae24eb86442e34d9ef6c8f3e4deac968
URL:		http://search.cpan.org/dist/HTML-Table/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::Table is used to generate HTML tables for CGI scripts. By using
the methods provided fairly complex tables can be created,
manipulated, then printed from Perl scripts. The module also greatly
simplifies creating tables within tables from Perl. It is possible to
create an entire table using the methods provided and never use an
HTML tag.

%description -l pl.UTF-8
HTML::Table służy do generowania tabelek w HTML-u z poziomu skryptów
CGI. Przy użyciu dostarczonych metod można tworzyć, obrabiać i
drukować dosyć skomplikowane tabele z poziomu skryptów perlowych.
Moduł także znakomicie upraszcza tworzenie tabelek w tabelkach. Można
stworzyć całą tabelę przy użyciu tych metod be użycia ani jednego
znacznika HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%doc Changes
%{perl_vendorlib}/HTML/Table.pm
%{_mandir}/man3/*
