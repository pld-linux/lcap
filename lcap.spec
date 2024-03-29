Summary:	Linux Capability Remover
Summary(pl.UTF-8):	Program do usuwania "capabilities" w kernelu
Summary(pt_BR.UTF-8):	Utilitário para alterar as capabilities do kernel
Name:		lcap
Version:	0.0.6
Release:	4
License:	GPL
Group:		Base
#Source0:	http://pweb.netcom.com/~spoon/lcap/download/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	3d6e7c160960b1621a6664c143757244
#URL:		http://pweb.netcom.com/~spoon/lcap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Removes "capabilities" in the kernel making the operating system more
secure.

%description -l pl.UTF-8
Usuwa "capabilities" z kernela, czyniąc system operacyjny bardziej
bezpiecznym.

%description -l pt_BR.UTF-8
Este utilitário permite que se altere as capabilities do kernel.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags} -Wall -DVERSION=%{version}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%{__make} install \
	prefix=$RPM_BUILD_ROOT

install lcap.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/lcap
%{_mandir}/man?/*
