from lxml.html.soupparser import fromstring

tree = fromstring("<a>Find me!</a>")
print tree.xpath("//a/text()")
