Summary:	Linux Capability Remover
Name:		lcap
Version:	0.0.2
License:	GPL
Release:	1
Group:		Base
Source:		http://pweb.netcom.com/~spoon/lcap/download/%{name}-%{version}.tar.bz2
URL:		http://pweb.netcom.com/~spoon/lcap/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sbindir	/sbin

%description
Removes "capabilities" in the kernel making the operating system
more secure.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall -DVERSION=%{version}"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/lcap
