from HTMLParser import HTMLParser
from urllib2 import urlopen
from urllib2 import urlparse
class myparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print 'tag: ', tag
	    #for attr in attrs:
            #print '   attr:', attr
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = urlparse.urljoin(self.baseurl, value)
                    self.links = self.links.union({newUrl})

    def handle_data(self, data):
        if '{' not in data:
            for keyword in self.keywords:
                if keyword in data:
                    print data

    def init(self, baseurl, keywords):
        self.links = set()
        self.baseurl = baseurl
        self.keywords = keywords

    def fetchUrl(self):
        response = urlopen(self.baseurl)
        if response.info().getheader('Content-type').startswith('text/html'):
            htmlString = response.read()
            self.feed(htmlString)