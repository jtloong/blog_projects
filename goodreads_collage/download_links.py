import urllib.request as ur 

raw_output = open("links.txt","r+").read()
raw_output = raw_output[1:-1].split('"')

links = [i for i in raw_output if i[:5] == 'https']


for i, link in enumerate(links):
	image = ur.urlopen(link)
	output = open("images/book" + str(i) + ".jpg","wb")
	output.write(image.read())
	output.close()