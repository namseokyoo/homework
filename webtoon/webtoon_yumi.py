import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

#메인 페이지에서, 최종화 정보 확인
data = requests.get('https://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=wed', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
toons = soup.select_one('#content .title > a')
epi = toons.get('href')

final_episode = epi.split("no=")[1].split("&")[0]
final =int(final_episode)
# 각 화의 링크를 돌며, 수집
# print(final_episode)
# print(type(final))


episode = 1
while episode <= final:

    data = requests.get(f'https://comic.naver.com/webtoon/detail.nhn?titleId=651673&no={episode}&weekday=wed',
                         headers=headers)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')
# select를 이용해서, img 들을 불러오기
    toons = soup.select('#comic_view_area > div > img')
# print(toons) 정상적으로 불러오는지 중간 체크용
# toon (img) 의 반복문을 돌리기
    print(episode, "화")
    for toon in toons:
    # toon 안에 src 불러오기
        yumi = toon.get('src')
        print(yumi)
    episode = episode + 1