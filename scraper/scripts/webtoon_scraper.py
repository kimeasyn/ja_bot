from bs4 import BeautifulSoup
import urllib.request as rq
from scraper.models import WebWebtoon


def run():
    """
    네이버 웹툰에서 인기 급상승 웹툰 10개 제목만 긁어서 저장
    실행 명령어: manage.py 가 있는 dir에서 [python manage.py runscript -v2 webtoon_scraper]
    """
    url = 'http://comic.naver.com/webtoon/weekday.nhn'
    # 크롤링할 주소
    res = rq.urlopen(url)
    # url에 해당하는 페이지를 브라우저에서 연것 처럼 수행
    soup = BeautifulSoup(res, "html.parser")
    # res에서 html요소들을 불러와서 파싱
    webtoon_title_html = soup.select('#realTimeRankFavorite > li > a')
    # 불러온 html요소들 중 li > div > a >  strong(네이버웹툰 - 인기 급상승 만화의 html selector) 에 해당하는 요소만 선택

    for html in webtoon_title_html:  # 여러개의 웹툰 제목들을 for문으로 각각 선택
        WebWebtoon.objects.create(
            title=html.get_text()    # html 태그를 제외한 제목 text 만 선택해서 저장
        )
