Summary: Linux Capability Remover
Name: lcap
Version: 0.0.1
Copyright: GPL
Release: 1
Group: System Environment/Base
Source: %{name}-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root

%description
Removes "capabilities" in the kernel making the operating system
more secure.

%prep
%setup -q

%build
make

%install
make install prefix=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}
cp COPYING README $RPM_BUILD_ROOT/usr/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc /usr/doc/*
/sbin/lcap

%changelog
* Fri Dec 10 1999 spoon <spoon@ix.netcom.com>
- created spec
