Summary:	Dump ABI of an ELF object containing DWARF debug info
Name:		abi-dumper
Version:	1.2
Release:	1
License:	LGPL v2.1+
Group:		Development/Tools
Source0:	https://github.com/lvc/abi-dumper/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e5ddc0ece3970ff0a34a984faac8e9f5
URL:		https://github.com/lvc/abi-dumper
BuildRequires:	perl-base >= 1:5.8
Requires:	binutils
Requires:	ctags
Requires:	elfutils
Requires:	gcc-c++
Requires:	perl-base >= 1:5.8
Requires:	vtable-dumper >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ABI Dumper - a tool to dump ABI of an ELF object containing DWARF
debug info.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}

%{__perl} Makefile.pl \
	-install \
	--prefix="%{_prefix}" \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/abi-dumper
