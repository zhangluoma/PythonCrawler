from myparser import myparser
parser = myparser()
parser.init('https://www.wsj.com/', ['Nasdaq'])
parser.fetchUrl()
#print parser.links
