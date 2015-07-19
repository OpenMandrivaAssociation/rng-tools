Summary:	Random number generator related utilities
Name:		rng-utils
Version:	5
Release:	3
Group:		System/Kernel and hardware
License:	GPLv2
Source0:	http://downloads.sourceforge.net/project/gkernel/rng-tools/5/rng-tools-%{version}.tar.gz

%description
Hardware random number generation tools.

%prep
%setup -qn rng-tools-%{version}
%apply_patches

%build
export CC=gcc
export CXX=g++

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

