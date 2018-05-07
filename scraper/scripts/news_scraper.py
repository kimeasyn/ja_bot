from bs4 import BeautifulSoup
import urllib.request as rq
from scraper.models import WebNews


def run():
    url = 'http://news.naver.com/'
    # 크롤링할 주소
    res = rq.urlopen(url)
    # url에 해당하는 페이지를 브라우저에서 연것 처럼 수행
    soup = BeautifulSoup(res, "html.parser")
    # res에서 html요소들을 불러와서 파싱
    news_title_html = soup.select('li > div > a > strong')
    # 불러온 html요소들 중 li > div > a >  strong 에 해당하는 요소만 선택

    for html in news_title_html:  # 여러개의 뉴스 제목들을 for문으로 각각 선택
        news_title = html.get_text()    # html 태그를 제외한 text만 선택
        WebNews.objects.create(         # text를 db에 저장
            title=news_title
        )
