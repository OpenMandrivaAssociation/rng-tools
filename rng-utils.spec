Summary:	Random number generator related utilities
Name:		rng-utils
Version:	2
Release:	15
Group:		System/Kernel and hardware
License:	GPLv2
Source0:	rng-tools-%{version}.tar.bz2
# 2.6.x's device name
Patch1:		rng-tools-2-devname.patch

%description
Hardware random number generation tools.

%prep
%setup -qn rng-tools-%{version}
%patch1 -p1

%build
%configure --sbindir=/sbin
%make

%install
mkdir -p %{buildroot}{%{_sbindir},%{_mandir}/man{1,8},%{_sysconfdir},%{_initrddir}}
%makeinstall_std
chmod -R a-s %{buildroot}

%files
%{_bindir}/rngtest
/sbin/rngd
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*

