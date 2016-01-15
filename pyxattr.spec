Name: 		pyxattr
Summary: 	Extended attributes library wrapper for Python
Version: 	0.5.0
Release: 	1%{?dist}
#license version is precised on a website
License: 	LGPLv2+
Group: 		Development/Libraries
URL: 		http://pyxattr.sourceforge.net/
Source:		http://downloads.sourceforge.net/pyxattr/pyxattr-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#python-xattr name was used in DAG repository
Provides:	python-xattr = %{version}-%{release}
Obsoletes:	python-xattr <= %{version}-%{release}
#libattr package is already forced by RPM
Requires: 	python >= 2.2
#python-setuptools package is required since 0.4.0
BuildRequires:	python-devel, libattr-devel, python-setuptools

%description
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_libdir}/python*/site-packages/xattr.so
#Python Eggs already in source distribution
#(without compiled content, can be simple included in RPM package)
%{_libdir}/python*/site-packages/*egg-info
%doc COPYING NEWS README

%changelog
* Sun Dec 27 2009 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.5.0-1
- updated to 0.5.0
- added support for unicode filenames (bug 479417)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 6 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.4.0-2
- added python-setuptools in BuildRequires which is needed in build process
since version 0.4.0 (thanks to Kevin Fenzi)

* Fri Dec 5 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.4.0-1
- updated to 0.4.0
- License Tag adjusted to current licensing LGPLv2+
- modified Python Eggs support due to its usage in source distribution 

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.2.2-4
- Rebuild for Python 2.6

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.2.2-3
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.2-2
- added compatibility with Python Eggs forced in F9 

* Mon Aug 27 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.2-1
- upgraded to 0.2.2

* Sun Aug 26 2007 Kevin Fenzi <kevin@tummy.com> - 0.2.1-5
 - Updated License tag

* Wed Apr 25 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-4
 - added Provides/Obsoletes tags

* Sat Apr 21 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-3
 - removed redundant after name change "exclude" tag
 - comments cleanup

* Wed Apr 18 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-2
 - applied suggestions from Kevin Fenzi
 - name changed from python-xattr to pyxattr
 - corrected path to the source file

* Thu Apr 5 2007 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 0.2.1-1
 - updated to 0.2.1
 - added python-devel in BuildRequires
 - added more doc files
 - added Provides section
 - modified to Fedora Extras requirements

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.2-1 - +/
- Initial package. (using DAR)
