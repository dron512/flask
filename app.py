from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# =============================================
# 더미 데이터: 넷플릭스 인기 영화/드라마 20개
# 각 항목: 제목, 장르, 평점, 포스터URL, 줄거리, 넷플릭스링크
# =============================================
MOVIES = [
    {
        "title": "오징어 게임",
        "genre": "스릴러/드라마",
        "rating": 9.2,
        "poster": "https://images.unsplash.com/photo-1611532736597-de2d4265fba3?w=400&q=80",
        "summary": "456억 원의 상금을 위해 목숨을 건 서바이벌 게임에 참가한 사람들의 이야기.",
        "link": "https://www.netflix.com/title/81040344"
    },
    {
        "title": "기생충",
        "genre": "스릴러/드라마",
        "rating": 9.0,
        "poster": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=400&q=80",
        "summary": "전원 백수인 기택 가족이 부유한 박 사장 가족에게 하나씩 침투하기 시작하는 이야기.",
        "link": "https://www.netflix.com/title/81054374"
    },
    {
        "title": "더 글로리",
        "genre": "드라마/복수",
        "rating": 8.9,
        "poster": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=400&q=80",
        "summary": "학교폭력 피해자가 가해자들에게 치밀하게 복수를 준비하는 이야기.",
        "link": "https://www.netflix.com/title/81518008"
    },
    {
        "title": "나르코스",
        "genre": "범죄/드라마",
        "rating": 8.8,
        "poster": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=400&q=80",
        "summary": "콜롬비아 마약왕 파블로 에스코바르의 실화를 바탕으로 한 범죄 드라마.",
        "link": "https://www.netflix.com/title/80025172"
    },
    {
        "title": "기묘한 이야기",
        "genre": "SF/공포/드라마",
        "rating": 8.7,
        "poster": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=400&q=80",
        "summary": "미국 소도시에서 초자연적 현상과 싸우는 아이들의 모험 이야기.",
        "link": "https://www.netflix.com/title/80057281"
    },
    {
        "title": "블랙 미러",
        "genre": "SF/스릴러",
        "rating": 8.6,
        "poster": "https://images.unsplash.com/photo-1516110833967-0b5716ca1387?w=400&q=80",
        "summary": "첨단 기술이 가져올 어두운 미래를 그린 옴니버스 SF 시리즈.",
        "link": "https://www.netflix.com/title/70264888"
    },
    {
        "title": "하우스 오브 카드",
        "genre": "정치/드라마",
        "rating": 8.5,
        "poster": "https://images.unsplash.com/photo-1541872703-74c5e44368f9?w=400&q=80",
        "summary": "권력을 향한 냉혹한 야망을 가진 정치인 프랜시스 언더우드의 이야기.",
        "link": "https://www.netflix.com/title/70178217"
    },
    {
        "title": "머니 하이스트",
        "genre": "범죄/액션",
        "rating": 8.5,
        "poster": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400&q=80",
        "summary": "천재 도둑 '교수'가 이끄는 팀이 조폐국과 중앙은행을 대담하게 강탈하는 이야기.",
        "link": "https://www.netflix.com/title/80192098"
    },
    {
        "title": "위처",
        "genre": "판타지/액션",
        "rating": 8.3,
        "poster": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400&q=80",
        "summary": "괴물 사냥꾼 게롤트가 운명으로 얽힌 공주 시리를 찾아 떠나는 판타지 서사시.",
        "link": "https://www.netflix.com/title/80189685"
    },
    {
        "title": "브리저튼",
        "genre": "로맨스/드라마",
        "rating": 8.1,
        "poster": "https://images.unsplash.com/photo-1502635385003-ee1e6a1a742d?w=400&q=80",
        "summary": "19세기 영국 상류사회를 배경으로 펼쳐지는 화려한 로맨스와 스캔들.",
        "link": "https://www.netflix.com/title/80232398"
    },
    {
        "title": "킹덤",
        "genre": "좀비/사극",
        "rating": 8.4,
        "poster": "https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=400&q=80",
        "summary": "조선시대를 배경으로 정체불명의 역병과 싸우는 세자의 이야기.",
        "link": "https://www.netflix.com/title/80170559"
    },
    {
        "title": "나의 해방일지",
        "genre": "로맨스/드라마",
        "rating": 8.6,
        "poster": "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?w=400&q=80",
        "summary": "평범한 일상에서 해방을 꿈꾸는 세 남매의 현실적인 성장 드라마.",
        "link": "https://www.netflix.com/title/81518000"
    },
    {
        "title": "수리남",
        "genre": "범죄/액션",
        "rating": 7.9,
        "poster": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=400&q=80",
        "summary": "마약왕을 잡기 위해 국정원의 작전에 투입된 평범한 사업가의 이야기.",
        "link": "https://www.netflix.com/title/81166929"
    },
    {
        "title": "D.P.",
        "genre": "군대/드라마",
        "rating": 8.2,
        "poster": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=400&q=80",
        "summary": "탈영병을 잡는 군 헌병대 소속 D.P. 팀의 이야기를 통해 군대 내 현실을 담은 드라마.",
        "link": "https://www.netflix.com/title/81166922"
    },
    {
        "title": "지옥",
        "genre": "SF/스릴러",
        "rating": 7.8,
        "poster": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400&q=80",
        "summary": "지옥의 사자가 나타나 사람들을 지옥으로 보내는 초자연적 현상이 일어나는 세상.",
        "link": "https://www.netflix.com/title/81456322"
    },
    {
        "title": "종이의 집: 공동경제구역",
        "genre": "범죄/액션",
        "rating": 7.6,
        "poster": "https://images.unsplash.com/photo-1580519542036-c47de6196ba5?w=400&q=80",
        "summary": "통일을 앞둔 한반도를 배경으로 한 대담한 강도단의 이야기.",
        "link": "https://www.netflix.com/title/81508812"
    },
    {
        "title": "에밀리, 파리에 가다",
        "genre": "로맨스/코미디",
        "rating": 7.4,
        "poster": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=400&q=80",
        "summary": "파리로 발령받은 미국인 마케터 에밀리의 유쾌한 직장·연애 이야기.",
        "link": "https://www.netflix.com/title/81037371"
    },
    {
        "title": "코브라 카이",
        "genre": "액션/드라마",
        "rating": 8.5,
        "poster": "https://images.unsplash.com/photo-1555597673-b21d5c935865?w=400&q=80",
        "summary": "가라데 키드의 30년 후, 라이벌 두 사람이 다시 도장을 열며 벌어지는 이야기.",
        "link": "https://www.netflix.com/title/81002370"
    },
    {
        "title": "수사반장 1958",
        "genre": "수사/드라마",
        "rating": 8.0,
        "poster": "https://images.unsplash.com/photo-1521986329282-0436c1f1e212?w=400&q=80",
        "summary": "1958년 한국을 배경으로 한 형사들의 뜨거운 수사 이야기.",
        "link": "https://www.netflix.com/title/81707002"
    },
    {
        "title": "카지노",
        "genre": "범죄/드라마",
        "rating": 8.3,
        "poster": "https://images.unsplash.com/photo-1606167668584-78701c57f13d?w=400&q=80",
        "summary": "필리핀 카지노를 무대로 한 한국인 범죄 조직의 생존과 배신 이야기.",
        "link": "https://www.netflix.com/title/81687824"
    },
]


# =============================================
# 라우트 1: 메인 페이지 렌더링
# =============================================
@app.route("/")
def index():
    return render_template("index.html")


# =============================================
# 라우트 2: 평점 높은 순 정렬 API
# GET /api/sorted -> 평점 내림차순 정렬된 JSON 반환
# =============================================
@app.route("/api/sorted")
def sorted_movies():
    sorted_list = sorted(MOVIES, key=lambda x: x["rating"], reverse=True)
    return jsonify(sorted_list)


# =============================================
# 라우트 3: 랜덤 추천 API
# GET /api/random -> 랜덤으로 1개 작품 JSON 반환
# =============================================
@app.route("/api/random")
def random_movie():
    pick = random.choice(MOVIES)
    return jsonify(pick)


# =============================================
# 앱 실행
# =============================================
if __name__ == "__main__":
    app.run(debug=True)
