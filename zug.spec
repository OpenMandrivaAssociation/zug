%define devname %mklibname zug -d

Name: zug
Version: 0.1.1
Release: 1
Source0: https://github.com/arximboldi/zug/archive/refs/tags/v%{version}.tar.gz
Summary: C++ library providing transducers
URL: https://sinusoid.es/zug/
License: BSL-1.0
Group: System/Libraries
BuildRequires: cmake
BuildArch: noarch

%description
zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They are extremely
lightweight, and can be used to express algorithms over pull-based sequences
(iterators, files) but also push based sequences (signals, events,
asynchronous streams) in a generic way.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C++

%description -n %{devname}
Development files (Headers etc.) for %{name}.

zug is a C++ library providing transducers. Transducers are composable
sequential transformations independent of the source. They are extremely
lightweight, and can be used to express algorithms over pull-based sequences
(iterators, files) but also push based sequences (signals, events,
asynchronous streams) in a generic way.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_prefix}/lib/cmake/*
