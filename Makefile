build:
	cd /rpm_packaging
	tar -cvzf gello-1.0.tar.gz gello-1.0 
	mv -f gello-1.0.tar.gz rpmbuild/SOURCES/gello-1.0.tar.gz
	rpmbuild -bb --define "debug_package %{nil}" rpmbuild/SPECS/gello.spec
reset:
	yum remove -y gello
	make build
