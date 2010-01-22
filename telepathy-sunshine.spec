Summary:	Gadu-Gadu connection manager for the Telepathy
Summary(pl.UTF-8):	Zarządca połączeń Gadu-Gadu dla Telepathy
Name:		telepathy-sunshine
Version:	0.1.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-sunshine/%{name}-%{version}.tar.gz
# Source0-md5:	b71637e980eb33ad77fead0ee0224253
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	python
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
Requires:	python-TwistedCore
Requires:	python-TwistedWeb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Gadu-Gadu functionality for Telepathy.

%description -l pl.UTF-8
Ten pakiet udostępnia funkcjonalność Gadu-Gadu dla Telepathy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/telepathy-sunshine
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.sunshine.service
%{_datadir}/telepathy/managers/sunshine.manager
%{py_sitescriptdir}/sunshine
