%global optflags %{optflags} -Oz

Summary:	Random number generator related utilities
Name:		rng-tools
Version:	6.16
Release:	1
Group:		System/Kernel and hardware
License:	GPLv2
Url:		https://github.com/nhorman/rng-tools
Source0:	https://github.com/nhorman/rng-tools/archive/%{name}-%{version}.tar.gz
Source2:	rngd.sysconfig
Source3:	90-hwrng.rules
Patch0:		rng-tools-jitterentropy-3.4.patch
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	systemd-rpm-macros
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(libcap)
BuildRequires:	jitterentropy-library-devel
%rename rng-utils
%systemd_requires

%description
Hardware random number generation tools.
It monitors a set of entropy sources,
and supplies entropy from them to the
system kernel's /dev/random machinery.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh

# a dirty hack so libdarn_impl_a_CFLAGS overrides common CFLAGS
sed -i -e 's/$(libdarn_impl_a_CFLAGS) $(CFLAGS)/$(CFLAGS) $(libdarn_impl_a_CFLAGS)/' Makefile.in

%configure \
	--without-rtlsdr \
	--without-pkcs11 \
	--without-nistbeacon \
	--without-qrypt

%make_build

%install
%make_install


# install systemd unit file
install -m0644 rngd.service -Dt %{buildroot}%{_unitdir}
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/rngd
install -D -m 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/90-hwrng.rules

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-rngd.preset << EOF
enable rngd.service
EOF

chmod -R a-s %{buildroot}

%post
%systemd_post rngd.service

%preun
%systemd_preun rngd.service

%postun
%systemd_postun_with_restart rngd.service

%files
%{_sysconfdir}/sysconfig/rngd
%{_udevrulesdir}/90-hwrng.rules
%{_bindir}/rngtest
%{_bindir}/randstat
%{_sbindir}/rngd
%{_presetdir}/86-rngd.preset
%{_unitdir}/*.service
%doc %{_mandir}/man1/rngtest.1.*
%doc %{_mandir}/man8/rngd.8.*
