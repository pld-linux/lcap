Summary:	Linux Capability Remover
Summary(pl):	Program do usuwania "capabilities" w kernelu
Name:		lcap
Version:	0.0.6
Release:	3
License:	GPL
Group:		Base
Group(cs):	Z·klad
Group(da):	Basal
Group(de):	Basis
Group(es):	Base
Group(fr):	Base
Group(is):	Grunnforrit
Group(it):	Base
Group(ja):	•Ÿ°º•π
Group(no):	Basis
Group(pl):	Podstawowe
Group(pt):	Base
Group(pt_BR):	Base
Group(ru):	‚¡⁄¡
Group(sl):	Osnova
Group(sv):	Bas
Group(uk):	‚¡⁄¡
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
%{__make} CFLAGS="%{rpmcflags} -Wall -DVERSION=%{version}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install lcap.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/lcap
%{_mandir}/man8/*
