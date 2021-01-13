Summary:	Random number generator related utilities
Name:		rng-tools
Version:	6.11
Release:	1
Group:		System/Kernel and hardware
License:	GPLv2
Url:		https://github.com/nhorman/rng-tools
Source0:	https://github.com/nhorman/rng-tools/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	systemd-macros
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	sysfsutils-devel
BuildRequires:	pkgconfig(libp11)
BuildRequires:	jitterentropy-library-devel
BuildRequires:	pkgconfig(jansson)
%rename rng-utils

%description
Hardware random number generation tools.
It monitors a set of entropy sources,
and supplies entropy from them to the
system kernel's /dev/random machinery.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh

%configure --without-rtlsdr
%make_build

%install
%make_install

# install systemd unit file
install -Dt %{buildroot}%{_unitdir} -m0644 rngd.service

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-rngd.preset << EOF
enable rngd.service
EOF

chmod -R a-s %{buildroot}

%files
%{_bindir}/rngtest
%{_sbindir}/rngd
%{_presetdir}/86-rngd.preset
%{_unitdir}/*.service
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*
