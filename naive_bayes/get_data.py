import requests
import pickle
from bs4 import BeautifulSoup

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '__cfduid=d0b045798ce7787756702d2e2d0c999bc1608728250; _ga=GA1.2.777234261.1608729775; _gid=GA1.2.1793921661.1608729775; _gat=1',
        'Host': 'mstajbakhsh.ir',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
    }

all_data = []
all_data_categories = []

def get_categories(soup):
    categories = []
    ul = soup.find('ul', {'class': 'post-category'})
    lis = ul.findAll('li')
    for li in lis:
        categories.append(li.text)

    return categories

def get_body(soup):
    return soup.find('div', {'class': 'post-body'})

def get_paragraphs(soup):
    result = ''
    body = get_body(soup)
    paragraphs = body.findAll('p')
    for paragraph in paragraphs:
        result = result + ' ' + paragraph.text
    
    return result

def add_to_dataset(categories, paragraphs):
    for category in categories:
        all_data.append(paragraphs)
        all_data_categories.append(category)

def parse_post_page(post_page):
    soup = BeautifulSoup(post_page, 'html.parser')
    categories = get_categories(soup)
    paragraphs = get_paragraphs(soup)
    add_to_dataset(categories, paragraphs)

def get_post_page(link):
    post_page = requests.get(link,
                        headers=headers)
    parse_post_page(post_page.text)
    
def parse_main_page(main_page):
    soup = BeautifulSoup(main_page, 'html.parser')
    articles = soup.findAll('article')

    for article in articles:
        post_title = article.find('h3', {'class': 'post-title'})
        link = post_title.find('a').get('href')
        get_post_page(link)

def request_main_page():
    main_page = requests.get('https://mstajbakhsh.ir/',
                        headers=headers)

    parse_main_page(main_page.text)

def request_other_pages():
    for i in range(2, 7):
        page = requests.get('https://mstajbakhsh.ir/page/' + str(i),
                            headers=headers)

        print(page)

        parse_main_page(page.text)

def write_data_to_file():
    f = open("data/data_multi_label.pkl", "wb")
    pickle.dump(all_data, f, pickle.HIGHEST_PROTOCOL)
    f.close()

    f = open("data/categories_multi_label.pkl", "wb")
    pickle.dump(all_data_categories, f, pickle.HIGHEST_PROTOCOL)
    f.close()

if __name__ == "__main__":
    request_main_page()
    request_other_pages()
    write_data_to_file()
