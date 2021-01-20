import requests
import bs4

# Get web page
page = requests.get("https://en.wikipedia.org/wiki/John_C._Breckinridge")

print(page.status_code)

soup = bs4.BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

title = soup.find_all("h1", {"id": "firstHeading"})[0]
print(title.get_text())