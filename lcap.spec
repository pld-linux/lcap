Summary:	Linux Capability Remover
Summary(pl):	Program do usuwania "capabilities" w kernelu
Name:		lcap
Version:	0.0.6
Release:	3
License:	GPL
Group:		Base
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/lcap
%{_mandir}/man8/*
