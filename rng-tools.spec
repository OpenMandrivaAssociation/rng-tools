Summary:	Random number generator related utilities
Name:		rng-tools
Version:	6.7
Release:	1
Group:		System/Kernel and hardware
License:	GPLv2
Url:	https://github.com/nhorman/rng-tools
Source0:	https://github.com/nhorman/rng-tools/archive/%{name}-%{version}.tar.gz
Source1:	rngd.service
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	systemd-macros
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	sysfsutils-devel
%rename rng-utils

%description
Hardware random number generation tools.

%prep
%autosetup -p1

%build
export CC=gcc
export CXX=g++
./autogen.sh

%configure --sbindir=/sbin
%make_build

%install
%make_install

# install systemd unit file
install -Dt %{buildroot}%{_unitdir} -m0644 %{SOURCE1}

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-rngd.preset << EOF
enable rngd.service
EOF

chmod -R a-s %{buildroot}

%files
%{_bindir}/rngtest
/sbin/rngd
%{_presetdir}/86-rngd.preset
%{_unitdir}/*.service
%{_mandir}/man1/rngtest.1.*
%{_mandir}/man8/rngd.8.*
