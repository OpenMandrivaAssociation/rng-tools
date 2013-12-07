Summary:        Random number generator related utilities
Name:           rng-utils
Version:        2
Release:        12
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
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}{%_sbindir,%_mandir/man{1,8},%_sysconfdir,%_initrddir}
%makeinstall_std
chmod -R a-s %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/rngtest
/sbin/rngd
%_mandir/man1/rngtest.1.*
%_mandir/man8/rngd.8.*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2-9mdv2011.0
+ Revision: 669427
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2-8mdv2011.0
+ Revision: 607368
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2-7mdv2010.1
+ Revision: 523922
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2-6mdv2010.0
+ Revision: 426941
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2-5mdv2009.1
+ Revision: 351558
- rebuild

  + Michael Scherer <misc@mandriva.org>
    - bunzip patch

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2-4mdv2009.0
+ Revision: 225322
- rebuild

* Mon Jan 28 2008 Thierry Vignaud <tv@mandriva.org> 2-3mdv2008.1
+ Revision: 159302
- fix  no-cleaning-of-buildroot %%install
- fix/simplify %%setup usage
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 24 2007 Thierry Vignaud <tv@mandriva.org> 2-2mdv2008.0
+ Revision: 70933
- use %%mkrel
- Import rng-utils




* Thu Jan 13 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 2-1mdk
- initial release
