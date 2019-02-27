from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_archive_end():
	result = requests.get("https://www.newyorker.com/magazine/fiction")
	c = result.content
	soup = BeautifulSoup(c, features="html5lib")
	root = soup.find(id='app-root')
	end = root.find_all("li", {"class": "Pagination__listItem___1hFiK"})[-1].text
	return end.replace(',', '')


# data = pd.DataFrame(columns=['date_issued', 'author', 'title', 'description', 'link'])

archive_end = get_archive_end()
print(archive_end)
pages = ['https://www.newyorker.com/magazine/fiction/page/' + str(i) for i in range(1, int(archive_end) + 1)]
issues = []
authors = []
titles = []
descriptions = []
links = []
dates = []
page_num = []

for index, page_link in enumerate(pages):
	print(str(index) + ' - ' + page_link)
	result = requests.get(page_link)
	c = result.content
	soup = BeautifulSoup(c, features="html5lib")

	root = soup.find(id='app-root')

	for piece in root.find_all("li", {"class": "River__riverItem___3huWr"}):    
	    
	    for i, element in enumerate(piece.find_all('a')):
	        if i == 0:
	            issues.append(element.text)
	        if i == 1:
	            titles.append(element.text)
	        if i == 3:
	            authors.append(element.text)
	    if len(authors) != len(issues):
	    	authors.append("")
	    try:
	    	descriptions.append(piece.find('h5').text)
	    except:
	    	descriptions.append("")
	    links.append('https://newyorker.com' + piece.find('h4').parent['href'])
	    dates.append(piece.find('h4').parent['href'][10:20])
	    page_num.append(index)



	data = pd.DataFrame(columns=['date_issued', 'author', 'title', 'description', 'link', 'page'])
	data['date_issued'] = dates
	data['issue'] = issues
	data['author'] = authors 
	data['title'] = titles 
	data['description'] = descriptions
	data['link'] = links
	data['page'] = page_num

	data.to_csv('new-yorker.csv', index=False)