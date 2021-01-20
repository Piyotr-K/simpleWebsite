import requests
import bs4

page = requests.get("https://piyotr.com/simpleWebsite")

print(page.status_code)

soup = bs4.BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

# print(list(soup.children))
# Find element by tag
# body = soup.find_all('body')
# print(body)
email = soup.find_all('h2')
print(email[0].get_text().strip())