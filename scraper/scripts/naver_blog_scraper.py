import json
from pprint import pprint
import os
from ja_bot import settings
import urllib.request
import urllib.parse
from scraper.models import NaverSearch


def run(args='강남역 맛집'):
    """
    네이버 블로그 검색 api를 이용해 블로그 검색 결과중 상위 10개 글의 제목과 링크 저장
    실행 명령어: python manage.py runscript -v2 restaurant_scraper --script-args "검색어"
    검색어 없이 python manage.py runscript -v2 restaurant_scraper 로 실행시 args 기본값인
    '강남역 맛집'으로 검색
    """
    # 숨김파일에서 네이버 api key값 읽어옴
    file = os.path.join(settings.BASE_DIR, 'secret', 'secret.json')
    data = open(file)
    keys = json.load(data)
    client_id = keys['naver_client']
    client_secret = keys['naver_secret']

    search_keyword = args  # 검색할 단어
    keyword = urllib.parse.quote(search_keyword) # 검색할 단어 => url에 변수로 포함시킬수 있도록 파싱
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword # 검색어가 포함된 요청 url
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    # 요청 url에 네이버 api 인증키 정보 포함

    response = urllib.request.urlopen(request)  # 요청 보내기
    rescode = response.getcode()  # http response 코드
    if (rescode == 200):  # 요청이 성공했을 떄
        response_body = response.read()
        items = json.loads(response_body.decode('utf-8'))['items']
        # 문자열 형태의 검색 결과 데이터를 접근하기 쉽게 json 형식으로 변환

        for item in items:
            title = item['title']  # 결과 데이터 중 블로그 제목
            title = title.split('</b>')[1]
            # 결과 데이터 블로그 제목에서 <b>검색어</br>(굵은 글씨 강조) 제거 후 나머지만
            link = item['link']
            # 결과 데이터 중 해당 글 링크
            link = link.replace("'", "")
            # 결과 글 링크에서 작은 따옴표(') 제거

            NaverSearch.objects.create(
                keyword=keyword,
                title=title,
                link=link
            )  # DB에 저장

    else:  # 요청이 실패 했을떄
        print("Error Code:" + rescode)