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
    dust_title = soup.select('#aqiwgtvalue')[0].get('title')  # 미세먼지 정도, 좋음/나쁨/보통 정보가 들어있는 html 요소
    dust_level = soup.select('#cur_pm25')[0].get_text()  # 미세먼지 수치
    micro_dust_level = soup.select('#cur_pm10')[0].get_text()  # 초미세먼지 수치

    WebDust.objects.create(
        status=dust_title,
        dust_level=dust_level,
        micro_dust_level=micro_dust_level
    )
