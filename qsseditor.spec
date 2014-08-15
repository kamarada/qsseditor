#
# spec file for package qsseditor
#
# Copyright (c) 2014 Kamarada Project, Aracaju, Brazil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://github.com/kamarada
#


%define version 0.5.5
Name:           qsseditor
Version:        %{version}
Release:        1
Summary:        QSS Editor
License:        GPL-3.0
Group:          System/Fhs
Source0:        qsseditor-%{version}.zip
Url:            http://sourceforge.net/projects/qsseditor/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      i586 x86_64
BuildRequires:  libqt4-devel
BuildRequires:  libqscintilla-devel
BuildRequires:  make
BuildRequires:  unzip
BuildRequires:  upx
Requires:	hicolor-icon-theme


%description
A tool to edit and preview Qt style sheets (QSS), made by Dmitry Baryshev

http://sourceforge.net/projects/qsseditor/


%prep
unzip %{SOURCE0}
cp qsseditor-%{version}/LICENSE.txt COPYING


%build
cd qsseditor-%{version}
qmake
make
cd ..


%install
cd qsseditor-%{version}
mkdir -p $RPM_BUILD_ROOT/usr/bin
pwd
ls -a
cp ./QssEditor $RPM_BUILD_ROOT/usr/bin/qsseditor
mkdir -p $RPM_BUILD_ROOT/usr/share/qsseditor
cp -R translations $RPM_BUILD_ROOT/usr/share/qsseditor/translations
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps/
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps/
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps/
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/
cp icons/qsseditor-16.png $RPM_BUILD_ROOT/usr/share/icons/hicolor/16x16/apps/qsseditor.png
cp icons/qsseditor-24.png $RPM_BUILD_ROOT/usr/share/icons/hicolor/24x24/apps/qsseditor.png
cp icons/qsseditor-32.png $RPM_BUILD_ROOT/usr/share/icons/hicolor/32x32/apps/qsseditor.png
cp icons/qsseditor-48.png $RPM_BUILD_ROOT/usr/share/icons/hicolor/48x48/apps/qsseditor.png
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1/
cp man/qsseditor.1 $RPM_BUILD_ROOT/usr/share/man/man1/qsseditor.1
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
cp qsseditor.desktop $RPM_BUILD_ROOT/usr/share/applications/qsseditor.desktop
cd ..


%files
%defattr(-,root,root)
%doc COPYING
/usr/bin/qsseditor
/usr/share/applications/qsseditor.desktop
/usr/share/qsseditor/
/usr/share/icons/hicolor/16x16/apps/qsseditor.png
/usr/share/icons/hicolor/24x24/apps/qsseditor.png
/usr/share/icons/hicolor/32x32/apps/qsseditor.png
/usr/share/icons/hicolor/48x48/apps/qsseditor.png
/usr/share/man/man1/qsseditor.1.gz


%changelog
* Sat Aug 09 2014 kamaradalinux@gmail.com
- Initial import from version 0.5.5
