import telegram
from ja_bot import settings
import os
import json
from scraper.models import WebWebtoon
# 크롤링한 뉴스 모델(db) import
from .common import get_today_date  # 오늘 날짜 생성 및 리턴 함수 import

def run():
    # pip install python-telegram-bot 로 파이썬 텔레그램 라이브러리 설치
    chat_id = ['602469918', '515138252'] # 텔레그램 유저 id 키값

    file = os.path.join(settings.BASE_DIR, 'secret', 'secret.json') # 숨김파일에서 텔레그램 인증키 import
    data = open(file)
    keys = json.load(data)
    key = keys['telegram_key']
    bot = telegram.Bot(token=key) # 텔레그램 인증키 값으로 텔레그램 봇 인스턴스 생성

    today = get_today_date()  # 오늘 날짜의 웹툰 데이터 select
    webtoon = WebWebtoon.objects.filter(save_at__year=today['year'],
                                           save_at__month=today['month'],
                                           save_at__day=today['day']).values('title')

    webtoon_text = ''
    for index, data in enumerate(webtoon): # 배열로 되어있는 오늘의 웹툰 정보 들을 한 문자열로 합치는 과정
        webtoon_text += str(index+1) + '. ' + data['title']
        webtoon_text += '\n'
        # 번호 + 웹툰 제목(화) + 개행문자(\n)

    text = """
==오늘의 웹툰==
%s
    """ % webtoon_text
    # %s 대신에 위에서 만든 오늘의 웹툰 정보 문자열 대체

    for id in chat_id:
        # chat_id 배열에 있는 유저(id)에게 텔레그램 메세지 전송
        bot.sendMessage(chat_id=id, text=text)
