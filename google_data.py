from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def check_and_remove_social_media(url):
    parsed_url = urlparse(url)
    if parsed_url.netloc.endswith('facebook.com'):
        return False
    elif parsed_url.netloc.endswith('youtube.com'):
        print("This URL belongs to YouTube.")
        return False
    elif parsed_url.netloc.endswith('linkedin.com'):
        print("This URL belongs to LinkedIn.")
        return False
    elif parsed_url.netloc.endswith('twitter.com'):
        return False
    else:
        return True

def search_links(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search

    #print (help(search))
    urls = []
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    

        urls.append(j)
    urls = list(filter(check_and_remove_social_media, urls))
    return urls


def scrape_p_tags(urls):
    all_text = ""
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all <p> tags and extract text
            p_tags = soup.find_all('p')
            for p_tag in p_tags:
                all_text += p_tag.get_text() + "\n"
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return all_text

def google_Data(query):  # main
    #query = "who is ms dhoni"
    urls=search_links(query)
    combined_text = scrape_p_tags(urls)
    return (combined_text)

if __name__ == '__main__':
    print(google_Data("who is MS Dhoni?"))
