import telegram
from ja_bot import settings
import os
import json
from scraper.models import WebMusic
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

    today = get_today_date()  # 오늘 날짜의 노래순위 데이터 select
    music_rank = WebMusic.objects.filter(save_at__year=today['year'],
                                         save_at__month=today['month'],
                                         save_at__day=today['day']).values('rank', 'singer', 'title')

    music_text = ''
    for index, data in enumerate(music_rank): # 배열로 되어있는 노래 순위 정보들을 한 문자열로 합치는 과정
        music_text += data['rank'] + '. ' + data['title'] + ' - ' + data['singer']
        music_text += '\n'
        # 순위 + 노래 제목 + 가수 + 개행문자(\n)

    text = """
==오늘의 노래순위==
%s
    """ % music_text
    # %s 대신에 위에서 만든 노래 순위 정보 문자열 대체

    for id in chat_id:
        # chat_id 배열에 있는 유저(id)에게 텔레그램 메세지 전송
        bot.sendMessage(chat_id=id, text=text)
