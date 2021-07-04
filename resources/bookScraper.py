import requests
from bs4 import BeautifulSoup

def parse_result(html):
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    titles = soup.find_all('a', href=True)
    rankings = soup.find_all('h4')

    for ranking in rankings:
        for string in ranking.strings:
            if "." in string:
                print(string.strip())

    all_titles = []
    all_authors = []
    for title in titles:
        if ('items' in title['href']) and (title.string != None):
            all_titles.append(title.string)
        
        if ('authors' in title['href']) and ('written' not in title['href']):
            all_authors.append(title.string)

    sources = []
    for src in images:
        buf = src['src']
        if ('amazon' not in buf) and ('login' not in buf):
            sources.append(buf)

    out = []
    for x in range(0, len(all_titles)):
        buf = str(x + 1) + ", " + all_titles[x] + ", " + all_authors[x] + ", " + sources[x] + "\n"
        out.append(buf)
    return out

def request_site(url):
    try:
        response = requests.get(url)
        # Checking if our request has been accepted
        if response.status_code == 200:
            return response.text
    # If not then return None (null)
    except requests.RequestException:
        return None

def write_items_to_file(items):
    f = open("top-books.txt", "w")
    f.writelines(items)
    f.close()


def main(page):
    url = 'https://thegreatestbooks.org/?page=' + str(page)
    print(f"Scraping the requested url: {url}")
    html = request_site(url)
    items = parse_result(html)

    write_items_to_file(items)

def menu():
    cli_menu = '''
    Welcome to bookScraper

    Current Site: thegreatestbooks.org

    Please enter a page number to scrape
    '''
    userChoice = input(cli_menu)

    while True:
        try:
            buf = int(userChoice)
            return buf
        except Exception:
            print("Uh oh not a number, defaulting to 1")
            return 1
pageNum = menu()
main(pageNum)