from datetime import date


def get_today_date():
    # 오늘 날짜 생성 및 return 해주는 함수
    year = date.today().year
    month = date.today().month
    day = date.today().day

    return {
        'year': year,
        'month': month,
        'day': day
    }