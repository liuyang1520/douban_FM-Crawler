import urllib2;

req = urllib2.Request("http://www.douban.com");
response = urllib2.urlopen(req);
the_page = response.read();

print(the_page);
