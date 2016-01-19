 # Export Server Device List to console from clipboard

import bs4
import pyperclip
import re

# import html from page source

html_text = pyperclip.paste()
html_soup = bs4.BeautifulSoup(html_text, 'html.parser')

# search html for device numbers

html_results = html_soup.find('td', id="summary_servers")
server_text = html_results.get_text()
regex_search = re.compile(r'\d\d\d\d\d\d') 
server_list = re.findall(regex_search, server_text)


# export device numbers into .txt (comma separated)
print('\n')
count = 0
for server in server_list:
	count += 1
	if count == len(server_list):
		print(server, end= "")
	else:
		print(server + ',', end="")

print('\n \n %d Servers \n' %count)
print('Love you lil Qwaffle Pootz!')
