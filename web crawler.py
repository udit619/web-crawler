import requests
from bs4 import BeautifulSoup

def spider(max_page):
    page=1
    name=input("Enter url of the page you want to crawl\n")
    site=input("Enter main side address\n")
    class_name=input("Enter the class name of the part whose info you want\n")
    while(page<=max_page):
        url= name +str(page)
        source_code=requests.get(url)
        p_text=source_code.text
        soup=BeautifulSoup(p_text,"html.parser")
        for link in soup.findAll('a',{'class':class_name}):
            #for getting the link
            # if the link is wrong just delete the site
            # href=link.get("href")
            href= site+ link.get('href')
            #title of that link
            title=link.string
            print(href)
            print("\n",title)
            get_data(href)
        page += 1

'''def get_data(href):
    source_code=requests.get(href)
    plain_text=source_code.text
    soup=BeautifulSoup(plain_text)
    for item_name in soup.findAll(container tag in quotes,{'class':'class name'}):
    print(item_name.string)
'''
max_page=int(input("Enter the maximum no. of pages you want to crawl\n"))
spider(max_page)


