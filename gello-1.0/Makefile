gello:
	go build -o gello

clean:
	rm gello

install:
	mkdir -p $(DESTDIR)/opt/hoge/settings
	install gello $(DESTDIR)/opt/hoge/gello
	mkdir -p $(DESTDIR)/usr/lib/systemd/system
	install gello.service $(DESTDIR)/usr/lib/systemd/system/gello.service
