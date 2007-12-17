%define name	ttcp
%define version	1.12
%define rel	3

Name: %{name}
Version: %{version}
Release: %mkrel %{rel}
Source0: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.c.bz2
Source1: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.1.bz2
Source2: ftp://ftp.sgi.com/sgi/src/ttcp/ttcp.README.bz2
Summary: A tool for testing TCP connections
Group: Monitoring
License: Public Domain

%description
ttcp is a tool for testing the throughput of TCP connections. Unlike
other tools which might be used for this purpose (such as FTP
clients), ttcp does not read or write data from or to a disk while
operating, which helps ensure more accurate results.

%prep
%setup -c -T

bzcat %{SOURCE0} > ttcp.c
bzcat %{SOURCE1} > ttcp.1
bzcat %{SOURCE2} > README
chmod 644 *

%build
%{__cc} $RPM_OPT_FLAGS -o ttcp ttcp.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir \
	$RPM_BUILD_ROOT%_mandir/man1
install -m 755 ttcp $RPM_BUILD_ROOT%_bindir
install -m 644 ttcp.1 $RPM_BUILD_ROOT%_mandir/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/*/*


