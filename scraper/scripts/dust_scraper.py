from bs4 import BeautifulSoup
import urllib.request as rq
from scraper.models import WebDust


def run():
    """
    서울시 대기오염 사이트에서  현재 미세먼지 정보 크롤링 하여 저장
    실행 명령어: manage.py 가 있는 dir에서 [python manage.py runscript -v2 dust_scraper]
    """
    url = 'http://aqicn.org/city/seoul/kr/'
    # 크롤링할 주소
    res = rq.urlopen(url)
    # url에 해당하는 페이지를 브라우저에서 연것 처럼 수행
    soup = BeautifulSoup(res, "html.parser")
    # res에서 html요소들을 불러와서 파싱
    dust_info = soup.select('#aqiwgtvalue')[0] # 미세먼지 정도, 좋음/나쁨/보통 정보가 들어있는 html 요소
    dust_level = dust_info.get_text() # html 의  text 값으로 있는 미세먼지 정도(숫자)
    dust_title = dust_info.get('title') # html 의  title 값으로 있는 미세먼지 기준정보(좋음/나쁨/보통)
    # 불러온 html요소들 중 li > div > a >  strong(네이버뉴스 - 오늘의 뉴스제목의 html selector) 에 해당하는 요소만 선택

    WebDust.objects.create(
        title=dust_title,
        level=dust_level
    )
