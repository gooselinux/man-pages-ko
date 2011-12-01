Summary: Korean(Hangul) Man(manual) Pages from the Korean Manpage Project
Name: man-pages-ko
Version: 20050219
Release: 17%{?dist}
License: Copyright only
Epoch: 2
Group: Documentation
#Vendor: Korean Manpage Project Team.
URL: http://man.kldp.org/
Source0: http://kldp.net/frs/download.php/1918/%{name}-%{version}.tar.gz
Source1: Man_Page_Copyright
#Source1:http://man.kldp.org/wiki/ManPageCopyright
Patch0: %{name}-%{version}.patch
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root
#Autoreqprov: false
BuildArchitectures: noarch
Summary(ko): 한글 Manpage 프로젝트에 의한 한글 Manpage 

%description
Korean translation of the official manpages from LDP and
another useful manpages from various packages. It's done
by the Korean Manpage Project <http://man.kldp.org> which
is maintained by Korean Manpage Project Team.

%description -l ko
한글 Manpage 프로젝트에서 비롯된 한글 Manpages.
이는 한글 Manpage 프로젝트 팀이 관리하는 한글 Manpage
프로젝트 <http://man.kldp.org>에 의한 것입니다.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p0 -b .bak
find . -name CVS -exec rm -rf {} \;
cp %{SOURCE1} COPYING

#conflict with man
rm -f ./man1/man.1 ./man1/whatis.1 ./man5/man.config.5 
#conflict with shadow-utils in Fedora 9
rm -f ./man8/vipw.8
#conflict with rpms in Fedora 9
rm -f ./man8/rpm.8 ./man8/rpm2cpio.8
# Bug 468501
rm -f ./man1/cpio.1

%build 
for i in `find . -type f -name \*.gz`; do
    gunzip $i
done
for i in 1 1x 2 3 4 5 6 7 8 9; do
    for j in `find . -type f -name \*.$i`; do
        case "$j" in 
            './man7/iso_8859-1.7' | './man7/iso_8859-7.7')
                #Already in UTF-8
                iconv -f UTF-8 -t UTF-8 $j -o $j.out
                cp -a $j.out $j
                rm $j.out
                gzip $j
                ;;
            *)
                iconv -f EUC-KR -t UTF-8 $j -o $j.out
                cp -a $j.out $j
                rm $j.out
                gzip $j
                ;;
        esac
    done
    for j in `find . -type f -name \*.$i.bak`; do
        rm -f $j
    done
done


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_mandir}/ko
cp -a man? $RPM_BUILD_ROOT%{_mandir}/ko/


%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root,root, -)
%doc COPYING
%{_mandir}/ko/man*/*

%changelog
* Wed Mar 03 2010 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-17
- Resolves: #555195 (for package wrangler).

* Wed Mar 03 2010 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-15
- Resolves: #555195
- Fixed Fedora 569430 (Wrong directory ownership)

* Tue Jan 14 2010 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-14
- Resolves: #555195
- Build for package wrangler.

* Thu Jan 14 2010 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-11
- Build for package wrangler.

* Wed Dec 16 2009 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-10
- Add full URL to source.
- Fixed the Source1 path.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2:20050219-9.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20050219-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:20050219-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-7
- Fix Bug 468501 - There were file conflicts when cheeking the packages 
  to be installed in Fedora-10-beta-x86_6.

* Mon Sep 15 2008 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-5
- Fix Bug 462197 -  File conflict between man-pages-ko and rpm

* Mon Aug 04 2008 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-4
- Fix the file conflict with rpm-4.5.90

* Tue Feb 05 2008 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-3
- Correct Licence information.
- Add Korean summary and description

* Tue Jan 08 2008 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-2
- Bug 427684: man-pages fileconflict
- Fix the conflict with vipw.8 (in shadow-utils)


* Thu Dec 06 2007 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-1
- Fix the conflict with man-1.6e-3.fc7

* Thu Dec 06 2007 Ding-Yi Chen <dchen at redhat dot com> - 2:20050219-0
- man7/iso_8859-1.7 and man7/iso_8859-7.7 are back.
- Upstream change version scheme.

* Mon Feb 05 2007 Parag Nemade <pnemade@redhat.com> - 1:1.48-15.2
- Rebuild of package as pert of Core/Extras Merge

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.48-15.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov 23 2004 Miloslav Trmac <mitr@redhat.com> - 1:1.48-15
- Recode also man.1x to UTF-8

* Mon Jun 21 2004 Alan Cox <alan@redhat.com>
- man isn't required (there are multiple man page readers), as per other
  man packages

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 1.48-11
- removed man.1 and man.config.5, because the latest man contains those manpages.

* Tue Oct 28 2003 Leon Ho <llch@redhat.com>
- convert to utf-8 on build time
- modify logic in install

* Sun May 04 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- do not include a Vendor: tag

* Thu Feb 20 2003 David Joo <djoo@redhat.com>
- bug #83614 fixed

* Mon Jan 27 2003 Jeremy Katz <katzj@redhat.com> 1:1.48-7
- add an epoch to fix upgrades from 8.0

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 David Joo <djoo@redhat.com>
- Spelling mistakes fixed in specfile
- bug #81420 fixed

* Fri Dec 20 2002 David Joo <djoo@redhat.com>
- Updated to New version
- sgid bug fixed <#79965>

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild in current collection instance

* Mon Aug 12 2002 Bill Nottingham <notting@redhat.com>
- fix group

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb  1 2002 Bill Nottingham <notting@redhat.com>
- remove %%post/%%preun; they cause errors
- s/%%{prefix}/%%{_mandir}/g

* Thu Jan 31 2002 David Joo <davidjoo@redhat.com>
- Rebuilt against RHL 8.0

* Sun Jun 3 2001 Bae, Sunghoon <plodder@kldp.org>
- removed ftpcount, ftpwho, ftpshut, proftpd man pages
  because proftpd has it 
- changed man cache directory to /var/cache/man

* Tue May 23 2000 KIM KyungHeon <tody@teoal.sarang.net>
- changed name of spec file
- added some contents of spec (for relocatable)
- modified korean description
- fixed using 'makewhatis' command
- fixed expression in %%files tag

* Sun Apr  23 2000 Bae, Sunghoon <plodder@kldp.org>
- modify .spec

* Sat Apr  22 2000 Chongkyoon, Rim <hermes44@secsm.org>
- modify .spec

* Tue Apr  4 2000 Bae, Sunghoon <plodder@kldp.org>
- First Release

