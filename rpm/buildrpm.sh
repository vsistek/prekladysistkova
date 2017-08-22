#!/bin/bash
set -x
cd `dirname $0`
cd ..

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

VERSION=`date -u +%Y%m%d%H%M`
cp rpm/prekladysistkova.spec ~/rpmbuild/SPECS/
sed -i "s/-VERSION-/$VERSION/g" ~/rpmbuild/SPECS/prekladysistkova.spec

rm ~/rpmbuild/SOURCES/prekladysistkova.tar.gz
mkdir ~/rpmbuild/SOURCES/prekladysistkova-1
cp -r www rb systemd nginx ~/rpmbuild/SOURCES/prekladysistkova-1/
( cd ~/rpmbuild/SOURCES/; tar cvzf prekladysistkova.tar.gz prekladysistkova-1 )
rm -r ~/rpmbuild/SOURCES/prekladysistkova-1
rm ~/rpmbuild/RPMS/noarch/*.rpm

rpmbuild -bb -v ~/rpmbuild/SPECS/prekladysistkova.spec

rm rpm/*.rpm
cp ~/rpmbuild/RPMS/noarch/*.rpm rpm/
