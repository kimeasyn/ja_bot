from bs4 import BeautifulSoup
import urllib.request as rq
from scraper.models import WebStock


def run():
    """
   네이버 현재 주식 크롤링 하여 저장
    실행 명령어: manage.py 가 있는 dir에서 [python manage.py runscript -v2 stock_scraper]
    """
    url = 'http://finance.naver.com/item/main.nhn?code=035420'
    # 크롤링할 주소
    res = rq.urlopen(url)
    # url에 해당하는 페이지를 브라우저에서 연것 처럼 수행
    soup = BeautifulSoup(res, "html.parser")
    # res에서 html요소들을 불러와서 파싱
    stock_price = soup.select('div > p.no_today')[0].find_all("span", {"class": "blind"})[0].get_text()
    stock_price = str(stock_price).replace(',', '')  # 금액 정보에서 콤마(,) 제거
    company_name = soup.select('#middle > div.h_company > div.wrap_company > h2 > a')[0].get_text()
    # 불러온 html요소들 중 l#middle > div.h_company > div.wrap_company > h2 > a
    # (네이버 금융 - 네이버주식 html selector) 에 해당하는 요소만 선택후 text값 파싱
    
    WebStock.objects.create(
        company=company_name,
        price=stock_price
    )
    # 테이블에 크롤링한 회사명, 주식 가격 입력
