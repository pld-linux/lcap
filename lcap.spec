Summary:	Linux Capability Remover
Summary(pl):	Program do usuwania "capabilities" w kernelu
Name:		lcap
Version:	0.0.6
Release:	1
License:	GPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	http://pweb.netcom.com/~spoon/lcap/download/%{name}-%{version}.tar.bz2
URL:		http://pweb.netcom.com/~spoon/lcap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Removes "capabilities" in the kernel making the operating system more
secure.

%description -l pl
Usuwa "capabilities" z kernela, czyni±c system operacyjny bardziej
bezpiecznym.

%prep
%setup -q

%build
%{__make} CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g} -Wall -DVERSION=%{version}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/lcap
