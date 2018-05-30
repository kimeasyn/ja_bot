import telegram
from ja_bot import settings
import os
import json
from scraper.models import WebDust # 크롤링 한 미세먼지 정보 모델(db) import
from .common import get_today_date  # 오늘 날짜 생성 및 리턴 함수 import


def run():
    # pip install python-telegram-bot 로 파이썬 텔레그램 라이브러리 설치
    chat_id = ['602469918', '515138252'] # 텔레그램 유저 아이디 키값
    file = os.path.join(settings.BASE_DIR, 'secret', 'secret.json')  # 숨김파일에서 텔레그램 인증키 import
    data = open(file)
    keys = json.load(data)
    key = keys['telegram_key']
    bot = telegram.Bot(token=key)  # 텔레그램 봇 토큰 키값으로 봇 인스턴스 생성

    today = get_today_date()  # 오늘 날짜의 미세먼지 데이터 select
    dust = WebDust.objects.filter(save_at__year=today['year'],
                                  save_at__month=today['month'],
                                  save_at__day=today['day']).first()
    text = """
===오늘의 미세먼지===
상태:%s \n
미세먼지(PM 2.5):%s \n
초미세먼지(PM 10):%s \n
    """ % (dust.status, dust.dust_level, dust.micro_dust_level)
    # %s 대신에 미세먼지 구분(문자), 레벨(숫자) 삽입

    for id in chat_id:
        # chat_id 배열에 있는 유저(id)에게 텔레그램 메세지 전송
        bot.sendMessage(chat_id=id, text=text)
