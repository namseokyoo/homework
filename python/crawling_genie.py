import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
musics = soup.select('#body-content > div > div > table > tbody > tr')

# print(musics)
# musics (tr들) 의 반복문을 돌리기
rank = 1
for music in musics:
    # music 안에 a 가 있으면, title과 artist 각각 불러오기
    title_tag = music.select_one('td.info > a.title.ellipsis')
    artist_tag = music.select_one('td.info > a.artist.ellipsis')

    if title_tag is not None:
        title = title_tag.text
        artist = artist_tag.text
    # 화면에 표시하고 랭킹 하나 올리기
        print(rank, title.strip(), artist)
        rank += 1
