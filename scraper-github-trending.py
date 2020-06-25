import requests



from bs4 import BeautifulSoup
# Collect the github 
page = requests.get('https://github.com/trending')
#print(page)
soup =BeautifulSoup(page.text, 'html.parser')

repo = soup.find(class_="Box-row")

# find all instances of that class (should return 25 as shown in the github main page)
#repo_list = repo.find_all(class_='col-12 d-block width-full py-4 border-bottom')
# find all instances of that class (should return 25 as shown in the github main page)
repo_list = soup.findAll(class_="col-9 text-gray my-1 pr-4")

print(repo_list)
