from django.db import models

# Create your models here.


class ApiWeather(models.Model):
    # API에서 받아온 날씨정보 저장 테이블
    # content = models.TextField()
    temp = models.CharField(max_length=10, verbose_name='기온')  # 현재 기온
    status = models.CharField(max_length=50, verbose_name='날씨')  # 날씨상태
    humidity = models.CharField(max_length=10, verbose_name='습도')  # 습도
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')  # 저장 시각, auto_now_add로 row 생성시 자동으로 현재 시각 저장
    send_at = models.DateTimeField(null=True)  # 발송시각, 저장후 발송전 데이터가 없을 수 있으므로 null 허용 옵션 추가

    class Meta:
        verbose_name = '날씨'
        verbose_name_plural = '날씨'


class ApiRestaurant(models.Model):
    # API에서 받아온 맛집정보 저장 테이블
    content = models.TextField()
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)


class WebMusic(models.Model):
    # 웹(멜론)에서 받아온 노래정보 저장 테이블
    rank = models.CharField(max_length=10, verbose_name='순위')
    title = models.TextField(verbose_name='제목')
    singer = models.CharField(max_length=50, verbose_name='가수')
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '노래순위'
        verbose_name_plural = '노래순위'
    

class WebNews(models.Model):
    # 웹(네이버 뉴스)에서 받아온 뉴스 저장 테이블
    title = models.TextField(verbose_name='뉴스제목')
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '뉴스'
        verbose_name_plural = '뉴스'
    
    
class WebWebtoon(models.Model):
    # 웹(네이버 웹툰)에서 받아온 웹툰 정보 저장 테이블
    title = models.TextField(verbose_name='웹툰')
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '웹툰'
        verbose_name_plural = '웹툰'


class WebStock(models.Model):
    # 네이버에서 네이버 주식 저장
    company = models.CharField(max_length=50, verbose_name='회사')
    price = models.IntegerField(verbose_name='주가')
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '주식'
        verbose_name_plural = '주식'


class WebDust(models.Model):
    # 미세먼지 정보 저장
    status = models.CharField(max_length=50, verbose_name='상태')  # 미세먼지 기준 정보(좋음/나쁨/보통)
    dust_level = models.SmallIntegerField(verbose_name='미세먼지 수치')  # 미세먼지 정도
    micro_dust_level = models.SmallIntegerField(verbose_name='초미세먼지 수치')  # 초미세먼지 정도
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '미세먼지'
        verbose_name_plural = '미세먼지'


class NaverSearch(models.Model):
    # 네이버 블로그 검색 api로 검색 결과
    keyword = models.CharField(max_length=100, verbose_name='키워드') # 블로그 검색어
    title = models.TextField(verbose_name='제목') # 블로그 검색 결과 글 제목
    link = models.TextField(verbose_name='링크') # 블로그 검색 결과 글 링크 주소
    save_at = models.DateTimeField(auto_now_add=True, verbose_name='수집&전송 시각')
    send_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name = '맛집&카페'
        verbose_name_plural = '맛집&카페'