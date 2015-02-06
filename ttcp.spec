Summary: A tool for testing TCP connections
Name: ttcp
Version: 1.12
Release: 16
URL:	ftp://ftp.sgi.com/sgi/src/ttcp/
Source0: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.c
Source1: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.1
Source2: ftp://ftp.sgi.com/sgi/src/ttcp/README
Patch0: ttcp-big.patch
Patch1: ttcp-malloc.patch
Patch2: ttcp-GNU.patch
Patch3: ttcp-man.patch
BuildRequires: glibc-devel
Group: Monitoring
License: Public Domain

%description
ttcp is a tool for testing the throughput of TCP connections.  Unlike other
tools which might be used for this purpose (such as FTP clients), ttcp does
not read or write data from or to a disk while operating, which helps ensure
more accurate results.

%prep
%setup -c -T -q
cp -a %{SOURCE0} %{SOURCE1} %{SOURCE2} .
%patch0 -p1 -b .big
%patch1 -p1 -b .malloc
%patch2 -p1 -b .GNU
%patch3 -p1 -b .man

%build
%{__cc} -o ttcp $RPM_OPT_FLAGS ttcp.c

%install
mkdir -p %{buildroot}{%{_mandir}/man1,%{_bindir}}
install -p -m755 ttcp %{buildroot}%{_bindir}
install -p -m644 ttcp.1 %{buildroot}%{_mandir}/man1

%files
%doc README
%{_bindir}/ttcp
%{_mandir}/man1/ttcp.1*
