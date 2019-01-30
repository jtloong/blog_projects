import urllib.request as ur 

output = open("links.txt","r+").read()
output = output[1:-1]
output = output.split('"')

links = []
for i in output:
	if len(i) > 5:
		links.append(i)

for i, link in enumerate(links):
	resource = ur.urlopen(link)
	output = open("images/book" + str(i) + ".jpg","wb")
	output.write(resource.read())
	output.close()