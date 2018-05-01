from pyowm import OWM
from scraper.models import ApiWeather


def run():
    key = 'e2c494a261332c4d92ed2500daa9cc7a'
    # https://home.openweathermap.org 에서
    # 트래픽관리, 회원관리 등을 위해 사이트 자체적으로 생성&발급받은 서비스 키

    owm = OWM(key)  # openweathermap 객체 생성
    obs = owm.weather_at_place('Seoul')  # 서울의 현재 날씨 정보
    weathers = obs.get_weather()         # 다양한 날씨 데이터에 접근 할 수 있도록 해주는 함수

    temper = weathers.get_temperature(unit='celsius')
    """
    현재 서울의 기온 정보
    unit = ('celsius': 섭씨, 'fahrenheit': 화씨)
    temper['temp']: 현재 온도
    temper['temp_max']: 최고 온도
    temper['temp_min']: 최저 온도
    """

    status = str.upper(weathers.get_status())  # 맑음/안개/구름 등의 현재 날씨 상태 데이터(영 대문자)
    kor_status = {
        'CLEAR': '맑음',
        'ClOUDS': '구름 많음', 'WIND': '구름',
        'HAZE': '안개', 'HUMIDITY': '습함',
        'RAIN': '비', 'SNOW': '눈'
    }  # status => 한글화

    humidity = str(weathers.get_humidity()) + '%'  # 습도

    ApiWeather.objects.create(
        temp=temper['temp'],  # 현재기온
        status=kor_status[status],  # 현재 날씨 상태
        humidity=humidity  # 현재 습도
    )
    """ 
    =insert into ApiWeather(temp, status, humidity) 
    values(temp, status, humidity)
    """



