import newspaper
import json
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse, urlunparse
from collections import *
import psycopg2
from psycopg2 import Error

def remove_url_hash(url):
    parsed_url = urlparse(url)
    clean_url = urlunparse(parsed_url._replace(fragment=''))
    return clean_url
def format_url(url):
    return remove_url_hash(url)

def get_text_content(url, input_html=None):
    article = newspaper.Article(url)
    article.download(input_html=input_html)
    article.parse()
    return article.text

# baseurl = 'https://python.langchain.com/docs/modules/agents/toolkits/document_comparison_toolkit'
# domain = 'https://python.langchain.com'
baseurl = 'https://www.vinmec.com/vi/tim-mach/tin-tuc-_hoat-dong/can-thiep-mach-vanh-chuan-my-tai-vinmec-nac-thang-moi-trong-dieu-tri-benh-tim-mach-tai-viet-nam/'
domain = 'https://www.vinmec.com/vi/'
postgredsn = "postgres://ubuntu:1@localhost:5432/langchain"
        
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(dsn=postgredsn)
    def insert(self, url, content):
        cursor = self.conn.cursor()
        try:
            cursor.execute("insert into crawl_webs(url, content) values(%s, %s)", (url, content))
            print("insert successfully", url)
        except (Exception, Error) as e:
            print("error ", e)
        cursor.close()
        self.conn.commit()


db = Database()

def crawl_websites(baseurl, domain):
    marked, dq, res, errors = set(), deque([baseurl]), [], []
    while dq:
        u = dq.popleft()
        if u in marked: continue
        marked.add(u)
        try:
            response = requests.get(u)
            htmlcontent = response.content.decode("utf-8")
            textcontent = get_text_content(u, input_html=htmlcontent)
            db.insert(u, textcontent)
            soup = BeautifulSoup(htmlcontent, parser='html.parser')
            bodytext = soup.body.get_text()
            for link in soup.find_all("a"):
                newu = urljoin(u, link.get("href",""))
                newu = format_url(newu)
                if newu in marked or not newu.startswith(domain): continue
                dq.append(newu)
        except (Exception, Error) as e:
            errors.append(dict(url=u, error = e))
    print(40, errors)
    return res

if __name__=="__main__":
    # print("-------------------------------------------------------\n\n", crawl_websites(baseurl, domain))
    crawl_websites(baseurl,domain)

