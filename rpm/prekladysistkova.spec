#
# spec file for package prekladysistkova
#
# Copyright (c) 2017 Vaclav Sistek
#

Name:           prekladysistkova
Version:	1
Release:	-VERSION-
Vendor:		Vaclav Sistek
License:	GPLv3
Summary:	prekladysistkova.cz website
Url:		http://www.prekladysistkova.cz/
Group:		Unspecified
Source:		prekladysistkova.tar.gz
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:	nginx ruby

%description
prekladysistkova.cz website files, sinatra app, systemd service, nginx configuration

%prep
%setup -q

%build


%install
rm -rf %{buildroot}

install -d	%{buildroot}/srv/www/prekladysistkova.cz
install -d	%{buildroot}/srv/www/prekladysistkova.cz/www
install -m 644	www/kontakt.html %{buildroot}/srv/www/prekladysistkova.cz/www/kontakt.html
install -m 644	www/anglictina.html %{buildroot}/srv/www/prekladysistkova.cz/www/anglictina.html
install -d	%{buildroot}/srv/www/prekladysistkova.cz/www/resources
install -d	%{buildroot}/srv/www/prekladysistkova.cz/www/resources/css
install -m 644	www/resources/css/main.css %{buildroot}/srv/www/prekladysistkova.cz/www/resources/css/main.css
install -d	%{buildroot}/srv/www/prekladysistkova.cz/www/resources/images
install -m 644	www/resources/images/favicon-ms.png %{buildroot}/srv/www/prekladysistkova.cz/www/resources/images/favicon-ms.png
install -m 644	www/resources/images/Babel.jpg %{buildroot}/srv/www/prekladysistkova.cz/www/resources/images/Babel.jpg
install -m 644	www/resources/images/MS.png %{buildroot}/srv/www/prekladysistkova.cz/www/resources/images/MS.png
install -d	%{buildroot}/srv/www/prekladysistkova.cz/rb
install -m 644	rb/prekladysistkova.rb %{buildroot}/srv/www/prekladysistkova.cz/rb/prekladysistkova.rb
install -d	%{buildroot}/etc/nginx/vhosts.d
install -m 644	nginx/prekladysistkova.cz.conf %{buildroot}/etc/nginx/vhosts.d/prekladysistkova.cz.conf
install -d	%{buildroot}/etc/systemd/system
install -m 644	systemd/prekladysistkova.service %{buildroot}/etc/systemd/system/prekladysistkova.service

%post
echo Installing rubygems
/usr/bin/gem install sinatra
/usr/bin/gem install pony

echo starting and enabling systemd service
/usr/bin/systemctl daemon-reload
/usr/bin/systemctl start prekladysistkova
/usr/bin/systemctl enable prekladysistkova

echo Reloading nginx.
/usr/bin/systemctl reload nginx

%files
%dir /srv/www/prekladysistkova.cz
%dir /srv/www/prekladysistkova.cz/www
%dir /srv/www/prekladysistkova.cz/www/resources
%dir /srv/www/prekladysistkova.cz/www/resources/css
%dir /srv/www/prekladysistkova.cz/www/resources/images
%dir /srv/www/prekladysistkova.cz/rb
%defattr(-,root,root)
/srv/www/prekladysistkova.cz/www/kontakt.html
/srv/www/prekladysistkova.cz/www/anglictina.html
/srv/www/prekladysistkova.cz/www/resources/css/main.css
/srv/www/prekladysistkova.cz/www/resources/images/favicon-ms.png
/srv/www/prekladysistkova.cz/www/resources/images/Babel.jpg
/srv/www/prekladysistkova.cz/www/resources/images/MS.png
/srv/www/prekladysistkova.cz/rb/prekladysistkova.rb
/etc/nginx/vhosts.d/prekladysistkova.cz.conf
/etc/systemd/system/prekladysistkova.service
