import telegram
from ja_bot import settings
import os
import json
from scraper.models import ApiWeather # 크롤링 한 날씨 모델(db) import
from .common import get_today_date  # 오늘 날짜 생성 및 리턴 함수 import


def run():
    # pip install python-telegram-bot 로 파이썬 텔레그램 라이브러리 설치
    chat_id = ['602469918', '515138252'] # 텔레그램 유저 아이디 키값
    file = os.path.join(settings.BASE_DIR, 'secret', 'secret.json')  # 숨김파일에서 텔레그램 인증키 import
    data = open(file)
    keys = json.load(data)
    key = keys['telegram_key']
    bot = telegram.Bot(token=key)  # 텔레그램 봇 토큰 키값으로 봇 인스턴스 생성

    today = get_today_date()  # 오늘 날짜의 날씨 데이터 select
    weather = ApiWeather.objects.filter(save_at__year=today['year'],
                                        save_at__month=today['month'],
                                        save_at__day=today['day']).first()
    text = """
===오늘의 날씨===
기온:%s \n
날씨:%s \n
습도:%s \n
    """ % (weather.temp, weather.status, weather.humidity)
    # %s 대신에 기온, 날씨상태, 습도 삽입

    for id in chat_id:
        # chat_id 배열에 있는 유저(id)에게 텔레그램 메세지 전송
        bot.sendMessage(chat_id=id, text=text)
