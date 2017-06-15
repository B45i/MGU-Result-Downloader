import urllib2, urllib, os
#Change the range according to register number
for i in xrange(1401XXXX, 140XXXX):
    data = urllib.urlencode({'exam': '59', 'prn': i})
    req = urllib2.Request('http://projects.mgu.ac.in/bTech/btechresult/index.php?module=public&attrib=result&page=result', data)
    print "downloading :%d.pdf" %i
    with open(os.path.basename("%d.pdf" %i), "wb") as local_file:
        local_file.write(urllib2.urlopen(req).read())