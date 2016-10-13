# retrieve links from a web page html

import urllib.request
with urllib.request.urlopen("http://www.iciba.com/") as conn:
    main_page = conn.read().decode("utf-8", errors="ignore")

# method 1
def get_child_urls(main_page, max_child=20):
    """retrieve urls from giving html page.
    args:
        main_page(str): html file.
        max_child(int): max number of return urls.
    return:
        list of url string.
    """
    from bs4 import BeautifulSoup, SoupStrainer
    children = []
    for link in BeautifulSoup(main_page, "html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'].startswith("http"):
            children.append(link['href'])
    if len(children) > max_child:
        children = children[:max_child]
    return children

a = get_child_urls(main_page)
print(a)




# method 2
from bs4 import BeautifulSoup
soup = BeautifulSoup(main_page, "html.parser")

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
