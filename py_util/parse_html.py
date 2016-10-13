# retrieve links from a web page html

import urllib.request
with urllib.request.urlopen("http://www.theverge.com/") as conn:
    main_page = conn.read().decode("utf-8", errors="ignore")


from bs4 import BeautifulSoup
soup = BeautifulSoup(main_page, "html.parser")

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
# print(soup.get_text())
# print("\n\ntext")
# print(soup.p.get_text())
# print("\nh")
# print(soup.h3.get_text())
# print(soup.h3.get_text())

print("\ntitle")
print(soup.title.string)
# for a in soup.find_all('title'):
#     print ("Found the URL:", a)

print("\nmeta")
# for meta in soup.findAll("meta"):
#     print (meta['name'], meta['content'])
for a in soup.find_all('meta'):
    if 'name' in a.attrs and (a['name'] == "description" or a['name']=='keywords'):
        print ("Found the URL:", a['content'])

print("\nh")
import re
for a in soup.find_all(re.compile("h[1-5]")):
    print ("Found the URL:", a.get_text())
    # print ("Found the URL:", a)

print("\np")
for a in soup.find_all('p'):
    print ("Found the URL:", a.get_text().strip())
