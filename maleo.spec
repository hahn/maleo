Name:    maleo
Version: 0.1.0
Release: 1%{?dist}
Summary: Maleo
URL:     http://dev.blankonlinux.or.id/browser/tambora/maleo
License: GPLv2

#Source0: http://arsip.blankonlinux.or.id/blankon/pool/main/m/maleo/maleo_%{version}.tar.gz
Source0: maleo-%{version}.tar.gz
Requires: glib-2.0 >= 2.12.0, gtk+-3.0 >= 3.0.8, webkitgtk-3.0 >= 1.3.0, seed >= 3.2.0, libxml-2.0 >= 2.9.1

%description
Maleo is a html5 application runner. This package provides HTML5 application runner.

%prep
%autosetup

%build
%configure
make

%install
%make_install

%files
%{_bindir}/maleo
#%{_bindir}/html5app
/usr/share/doc/maleo/AUTHORS
/usr/share/doc/maleo/COPYING
/usr/share/doc/maleo/ChangeLog
/usr/share/doc/maleo/INSTALL
/usr/share/doc/maleo/NEWS
/usr/share/doc/maleo/README


%changelog
