Summary:	Linux Capability Remover
Name:		lcap
Version:	0.0.1
License:	GPL
Release:	1
Group:		Base
Source:		http://pweb.netcom.com/~spoon/%{name}-%{version}.tar.bz2
URL:		http://pweb.netcom.com/~spoon/lcap.html
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_sbibdir	/sbin

%description
Removes "capabilities" in the kernel making the operating system
more secure.

%prep
%setup -q

%build
make

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
