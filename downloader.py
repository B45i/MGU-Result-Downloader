import urllib2, urllib, os
from PyPDF2 import PdfFileMerger



merger = PdfFileMerger()

r_start = 14019861
r_end 	= 14019986
exam 	= 72

for i in range(r_start, r_end+1):
	data = urllib.urlencode({'exam': '%d' %exam, 'prn': i})
	req = urllib2.Request('http://projects.mgu.ac.in/bTech/btechresult/index.php?module=public&attrib=result&page=result', data)
	print 'downloading :%d.pdf' %i
	with open(os.path.basename("%d.pdf" %i), "wb") as local_file:
		local_file.write(urllib2.urlopen(req).read())
		local_file.close()
	with open(os.path.basename("%d.pdf" %i), "rb") as local_file:
		try:
			merger.append(local_file)
			local_file.close()
		except:
			print '%d don\'t have result' %i

with open('result.pdf', 'wb') as fout:
    merger.write(fout)
