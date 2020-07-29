import requests
from bs4 import BeautifulSoup

url = 'http://www.pngmart.com/sitemapindex.xml/'

main_site_response = requests.get(url).text

soup = BeautifulSoup(main_site_response, 'xml')

pages = []

for loc in soup.find_all('loc'):
    url = loc.text
    if 'part' in url:
        pages.append(loc.text)

page1 = requests.get(pages[0]).text
soup = BeautifulSoup(page1, 'xml')
inner_pages = soup.find_all('loc')

for img_pages in inner_pages[0:5]:
    img_pages_txt      = img_pages.text
    image_page_content = requests.get(img_pages.text).text
    soup               = BeautifulSoup(image_page_content, 'html.parser')
    png                = soup.find('a',{'class':'download'})['href']
    image              = requests.get(png)
    image_title        = png.split('/')[-1]
    
    with open(image_title, 'wb') as file:
        file.write(image.content)
        
    print(png)