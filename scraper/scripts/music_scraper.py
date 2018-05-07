from bs4 import BeautifulSoup
import urllib.request as rq
import requests
from scraper.models import WebMusic


def run():
    """
    네이버 웹툰에서 인기 급상승 웹툰 10개 제목만 긁어서 저장
    실행 명령어: manage.py 가 있는 dir에서 [python manage.py runscript -v2 webtoon_scraper]
    """
    melon = requests.get('https://www.melon.com/chart/index.htm')  # 멜론차트 웹사이트
    melon_html = melon.text                                        # 멜론 차트의 html 구성
    melon_parse = BeautifulSoup(melon_html, 'html.parser')         # 멜론 차트의 html 구성을 html 파싱
    title_html = melon_parse.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
    # 멜론 차트의 노래 제목 html selector 선택
    singer_html = melon_parse.select('#lst50 > td > div > div > div.ellipsis.rank02 > span')
    # 멜론 차트의 가수 html selector 선택

    for index in range(10):     # 노래, 가수 배열에서 각각 10개 까지만 선택하도록 0~9 까지의 숫자 생성
        WebMusic.objects.create(
            rank=index + 1, # 배열은 0부터 시작이므로 +1 해줘야함
            title=title_html[index].get_text(), # 노래 목록중 index 번째 노래 선택
            singer=singer_html[index].get_text() # 가수 목록중 index 번째 가수 선택
        )
