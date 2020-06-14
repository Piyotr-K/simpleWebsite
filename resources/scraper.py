import requests
import bs4

page = requests.get("https://piyotr.com/simpleWebsite")

print(page.status_code)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

# print(list(soup.children))

# print([type(item) for item in list(soup.children)])
# ['html', '/n', 'contents of the webpage']

# html = list(soup.children)[2] # Take the last item (content) in the soup and put it in a variable

# body = list(html.children)[3] # Take just the body element

# print(list(body.children))

headings = soup.find_all('h2')

print(headings[0].get_text()) # text of the element
