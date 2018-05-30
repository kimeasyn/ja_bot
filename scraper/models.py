from django.db import models

# Create your models here.


class ApiWeather(models.Model):
    # API에서 받아온 날씨정보 저장 테이블
    # content = models.TextField()
    temp = models.CharField(max_length=10)  # 현재 기온
    status = models.CharField(max_length=50)  # 날씨상태
    humidity = models.CharField(max_length=10)  # 습도
    save_at = models.DateTimeField(auto_now_add=True)  # 저장 시각, auto_now_add로 row 생성시 자동으로 현재 시각 저장
    send_at = models.DateTimeField(null=True)  # 발송시각, 저장후 발송전 데이터가 없을 수 있으므로 null 허용 옵션 추가


class ApiRestaurant(models.Model):
    # API에서 받아온 맛집정보 저장 테이블
    content = models.TextField()
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)


class WebMusic(models.Model):
    # 웹(멜론)에서 받아온 노래정보 저장 테이블
    rank = models.CharField(max_length=10)
    title = models.TextField()
    singer = models.CharField(max_length=50)
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)
    

class WebNews(models.Model):
    # 웹(네이버 뉴스)에서 받아온 뉴스 저장 테이블
    title = models.TextField()
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)
    
    
class WebWebtoon(models.Model):
    # 웹(네이버 웹툰)에서 받아온 웹툰 정보 저장 테이블
    title = models.TextField()
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)


class WebStock(models.Model):
    # 네이버에서 네이버 주식 저장
    company = models.CharField(max_length=50)
    price = models.IntegerField()
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)


class WebDust(models.Model):
    # 미세먼지 정보 저장
    status = models.CharField(max_length=50)  # 미세먼지 기준 정보(좋음/나쁨/보통)
    dust_level = models.SmallIntegerField()  # 미세먼지 정도
    micro_dust_level = models.SmallIntegerField()  # 초미세먼지 정도
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)


class NaverSearch(models.Model):
    # 네이버 블로그 검색 api로 검색 결과
    keyword = models.CharField(max_length=100) # 블로그 검색어
    title = models.TextField() # 블로그 검색 결과 글 제목
    link = models.TextField() # 블로그 검색 결과 글 링크 주소
    save_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(null=True)