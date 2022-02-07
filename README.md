# With_Corona_Guide

위드 코로나를 극복하기 위한 사용자 맞춤형 위치 기반 다중이용시설 가이드 웹 서비스 프로젝트입니다.

# 목적

- 주기적으로 변화하는 거리두기 규율로 국민들이 혼란을 겪는 문제 발생
- 위드코로나에 맞추어 백신 접종 여부에 따른 이용시설 규제 정보 파악 필요

## 프레임워크

Django
- 쉽고 빠른 개발
- 풍부한 라이브러리 : 데이터 파싱, 분석, API 연동 등 활용 가능한 라이브러리 多

## 핵심 서비스

 - 위치 기반 다중 이용 시설 정보 제공
 - 다중 이용시설의 코로나 행동 명령 관련 정보 제공
 - 해외 여행이 가능한 나라들에 대한 정보제공
 - 위드 코로나 단계별 규율 정보 제공

## 위드 코로나 가이드 소개

- 메인페이지
![image](https://user-images.githubusercontent.com/92852871/152840409-6e088e5e-3831-4f07-8bed-8630454ee449.png)

- 사용자 위치 및 거리두기 정보
![image](https://user-images.githubusercontent.com/92852871/152840584-b7d27045-668c-4578-a7aa-b6e383ca1942.png)

- 이용시설 정보
![image](https://user-images.githubusercontent.com/92852871/152840653-4be0ad4a-9422-4ac2-8c01-beb9707d00fd.png)

- 해외 여행 정보
![image](https://user-images.githubusercontent.com/92852871/152840725-902f6333-6266-4452-b2d7-e4d89ba3502d.png)

## 구현 부분

- google map open api를 활용하여 사용자의 위치 지도가 사이트에 출력되도록 구현

```
# python http 라이브러리
import requests
```

```
# geocode.py 함수 구현
def gc():
    API_KEY = 

    address = '구래역'

    params = {
        'key': API_KEY,
        'address': address
    }

    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    response = requests.get(base_url, params=params).json()
    response.keys()

    if response['status'] == 'OK':
        geometry = response['results'][0]['geometry']
        lat = geometry['location']['lat']
        lon = geometry['location']['lng']
    return lat, lon
```

```
# views.py에서 gc() 함수 호출 및 intro.html로 반환값 전달
def intro(request):
    lat, lon = gc()
    return render(request, 'home/intro.html', {'lat': lat, 'lon' : lon})
```


