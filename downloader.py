#http://eecs.oregonstate.edu/sites/eecs.oregonstate.edu/files/cs101.pdf

import http.client
from time import sleep

for each in range(101, 999):
	conn = http.client.HTTPConnection("eecs.oregonstate.edu")
	document = "cs{0}.pdf".format(each)
	conn.request("GET", "/sites/eecs.oregonstate.edu/files/" + document )
	res = conn.getresponse()
	data = res.read()
	print(each)
	if (res.status == 200):
		print(document)
		f = open(document, "wb")
		f.write(data)
		f.close()
	conn.close()