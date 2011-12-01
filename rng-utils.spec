Summary:        Random number generator related utilities
Name:           rng-utils
Version:        2
Release:        %mkrel 9
Group:          System/Kernel and hardware
License:        GPL
Source0:        rng-tools-%version.tar.bz2
# 2.6.x's device name
Patch1:         rng-tools-2-devname.patch
Buildroot:      %_tmppath/%name-%version-root


%description
Hardware random number generation tools.

%prep
%setup -q -n rng-tools-%version
%patch1 -p1

%build
%configure --sbindir=/sbin
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}{%_sbindir,%_mandir/man{1,8},%_sysconfdir,%_initrddir}
%makeinstall_std
chmod -R a-s %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/rngtest
/sbin/rngd
%_mandir/man1/rngtest.1.*
%_mandir/man8/rngd.8.*
