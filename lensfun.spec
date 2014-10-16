Summary:	Camera lens database with image correction support
Name:		lensfun
Version:	0.2.8
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://download.berlios.de/lensfun/%{name}-%{version}.tar.bz2
# Source0-md5:	db2988505e7432c6b331aa597789c639
URL:		http://developer.berlios.de/projects/lensfun/
BuildRequires:	cmake
BuildRequires:	glib-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The project provides a database of photographic lenses and a library
that allows advanced access to the database including functions to
correct images based on intimate knowledge of lens characteristics and
calibration data.

%package devel
Summary:	lensfun library header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
lensfun library header files.

%package apidocs
Summary:	lensfun library API documentation
Group:		Documentation

%description apidocs
lensfun library API documentation.

%prep
%setup -q

%{__sed} -i "s|SET(LIBDIR lib)|SET(LIBDIR %{_lib})|" CMakeLists.txt

%build
install -d build
cd build
%cmake .. \
	-DLIBDIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

/usr/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tfun
%attr(755,root,root) %{_bindir}/trwxml
%attr(755,root,root) %ghost %{_libdir}/liblensfun.so.?
%attr(755,root,root) %{_libdir}/liblensfun.so.*.*.*
%{_datadir}/lensfun

%files devel
%defattr(644,root,root,755)
%{_includedir}/lensfun
%{_libdir}/liblensfun.so
%{_pkgconfigdir}/lensfun.pc

%files apidocs
%defattr(644,root,root,755)

