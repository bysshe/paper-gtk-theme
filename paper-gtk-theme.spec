# Spec file for package paper-gtk-theme
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

Name:           paper-gtk-theme
Version:        0.1
Release:        2%{?dist}

Summary:        Paper GTK Theme
License:        GPL-3.0+

Group:  User Interface/Desktops
Url:    http://snwh.org/paper/ 
Source: %{name}-%{version}.tar.gz

BuildArch:      noarch


%description
Paper GTK3 Theme, based upon Google's Material design from Android.

%prep
%setup -q

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Paper/ $RPM_BUILD_ROOT%{_datadir}/themes/

%files
%doc AUTHORS LICENSE
%{_datadir}/themes/Paper/

%changelog
* Sun Apr 05 2015 Liam Bulkley <liam@fightingcrane.com> 0.1-2
- new package built with tito
titofied for fedora copr

