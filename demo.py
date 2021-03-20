
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story 2</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0L1x0DM4mpSt97%2ftYgbxlC2B7n4pvJNhhvRwo8bxiO4B" class="sister" id="link1">Elsie</a>,
<a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0OPun6GIXb9bh0UOloN9WCYbJtHZQd%2fvB08D2UeudkPP" class="sister" id="link2">Lacie</a> and
<a href="/redirect?Id=f%2fKgPq4IDV0SyEq0zfYr0LirHL60gbBHH3VIishi9CqgtHAKmbGoKNvFheNkumnh" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""



from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())
# print (soup.title.string)
# print (soup.title)
# print (soup.p['class'])
print (soup.p.string)
# print (soup.a)
# print (soup.find_all('a'))
# print (soup.find(id="link3"))

# for link in soup.find_all('a'):
#     print (link.get('href')

print(soup.get_text())
