import telegram
from ja_bot import settings
import os
import json
from scraper.models import WebNews
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

    today = get_today_date()  # 오늘 날짜의 뉴스 데이터 select
    news = WebNews.objects.filter(save_at__year=today['year'],
                                  save_at__month=today['month'],
                                  save_at__day=today['day']).values('title')
    news_text = ''
    for index, a in enumerate(news): # 배열로 되어있는 뉴스 제목들을 한 문자열로 합치는 과정
        news_text += str(index+1) + '. ' + a['title'] # 배열 index(번호) + 뉴스 제목 + 개행문자(\n)
        news_text += '\n'

    text = """
==오늘의 뉴스==
%s
    """ % news_text
    # %s 대신에 위에서 만든 뉴스 제목 문자열 대체

    for id in chat_id:
        # chat_id 배열에 있는 유저(id)에게 텔레그램 메세지 전송
        bot.sendMessage(chat_id=id, text=text)
