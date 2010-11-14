# TODO
# - how to (where to?) package web and xml and index.html
%include	/usr/lib/rpm/macros.java
Summary:	ADT Plugin for Eclipse
Name:		eclipse-plugin-adt
Version:	0.9.9
Release:	0.4
License:	EPL v1.0
Group:		Libraries/Java
Source0:	http://dl.google.com/android/ADT-%{version}.zip
# Source0-md5:	7deff0c9b25940a74cea7a0815a3bc36
URL:		http://developer.android.com/sdk/eclipse-adt.html
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	eclipse >= 3.3
Requires:	eclipse-gef
Requires:	eclipse-jdt
Requires:	eclipse-plugin-webtools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
Android Development Tools (ADT) is a plugin for the Eclipse IDE that
is designed to give you a powerful, integrated environment in which to
build Android applications.

%prep
%setup -qc
find -name '*.jar' | while read jar; do
	dir=${jar%.jar}
	install -d $dir
	%{__unzip} -qq $jar -d $dir
	rm $jar
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/com.android.ide.eclipse.*
%{eclipsedir}/plugins/com.android.ide.eclipse.*
