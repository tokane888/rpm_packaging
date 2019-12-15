Name:           gello
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in golang

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
#BuildRequires:  systemd-rpm-macros

%description
hogehoge

%prep
echo $1
%setup

%build
echo $1
make %{?_smp_mflags}

%install
%make_install
chown fuga:fuga /opt/hoge

%post
%systemd_post %{name}.service

%pre

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service
# パッケージupdate時にパッケージ側でrestartかける場合は以下
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%attr(0744, fuga, fuga) /opt/hoge/%{name}
%{_unitdir}/%{name}.service

%changelog
* Sat Dec 14 2019 tokane888<tokane888@gmail.com> - 1.0-1
- First gello package
