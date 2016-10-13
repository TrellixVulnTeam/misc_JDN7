import eatiht.etv2 as etv2

url = "http://sputniknews.com/middleeast/20141225/1016239222.html"

tree = etv2.extract(url)

# we know what this does...
# print tree.get_text()

# add necessary link tags to bootstrap cdn, center content, etc.
tree.bootstrapify()

print (tree.get_html_string())
