from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GameRequest(BaseModel):
    genre: str         # 장르
    play_time: str     # 하루 플레이 시간
    platform: str      # 플랫폼

# 게임 추천 데이터
GAME_DB = {
    ("액션", "1시간 미만", "PC"): [
        {"title": "Hades", "reason": "짧은 런으로 즐길 수 있는 중독성 높은 로그라이크 액션"},
        {"title": "Hotline Miami", "reason": "빠르고 강렬한 짧은 플레이에 최적화된 액션"},
    ],
    ("액션", "1시간 미만", "콘솔"): [
        {"title": "Celeste", "reason": "짧은 스테이지 구성으로 틈틈이 즐기기 좋은 플랫포머"},
        {"title": "Shovel Knight", "reason": "스테이지별 클리어 방식으로 짧게 즐기기 적합"},
    ],
    ("액션", "1~3시간", "PC"): [
        {"title": "Devil May Cry 5", "reason": "화려한 콤보 액션, 스테이지 단위 플레이에 적합"},
        {"title": "Sekiro", "reason": "집중도 높은 전투 시스템, 도전적인 액션 게임"},
    ],
    ("액션", "1~3시간", "콘솔"): [
        {"title": "God of War", "reason": "압도적인 스토리와 액션, 콘솔 최고의 경험"},
        {"title": "Bayonetta 3", "reason": "화려하고 스타일리시한 콘솔 액션의 정수"},
    ],
    ("액션", "3시간 이상", "PC"): [
        {"title": "Elden Ring", "reason": "광활한 오픈월드와 도전적인 전투가 결합된 명작"},
        {"title": "Monster Hunter World", "reason": "몬스터 사냥의 깊은 재미, 장시간 플레이에 최적"},
    ],
    ("액션", "3시간 이상", "콘솔"): [
        {"title": "The Last of Us Part II", "reason": "영화 같은 스토리와 긴장감 넘치는 액션"},
        {"title": "Ghost of Tsushima", "reason": "아름다운 오픈월드와 사무라이 액션의 조화"},
    ],
    ("RPG", "1시간 미만", "PC"): [
        {"title": "Undertale", "reason": "짧은 세션으로 즐길 수 있는 감동적인 인디 RPG"},
        {"title": "Stardew Valley", "reason": "하루 일과 단위로 자연스럽게 끊을 수 있는 힐링 RPG"},
    ],
    ("RPG", "1시간 미만", "콘솔"): [
        {"title": "Pokémon Scarlet/Violet", "reason": "짧은 세션에도 목표를 정해 즐길 수 있는 포켓몬 RPG"},
        {"title": "Octopath Traveler", "reason": "챕터 단위로 짧게 끊기 좋은 턴제 RPG"},
    ],
    ("RPG", "1~3시간", "PC"): [
        {"title": "Baldur's Gate 3", "reason": "깊이 있는 선택지와 전략적 턴제 전투의 최고봉"},
        {"title": "Disco Elysium", "reason": "독특한 세계관과 방대한 선택지의 텍스트 RPG"},
    ],
    ("RPG", "1~3시간", "콘솔"): [
        {"title": "Persona 5 Royal", "reason": "스타일리시한 턴제 RPG, 세션 단위 진행에 적합"},
        {"title": "Final Fantasy XVI", "reason": "박진감 넘치는 스토리와 액션 RPG의 조화"},
    ],
    ("RPG", "3시간 이상", "PC"): [
        {"title": "Cyberpunk 2077", "reason": "방대한 오픈월드와 깊은 스토리, 장시간 몰입에 최적"},
        {"title": "The Witcher 3", "reason": "역대 최고의 오픈월드 RPG, 수백 시간의 콘텐츠"},
    ],
    ("RPG", "3시간 이상", "콘솔"): [
        {"title": "Xenoblade Chronicles 3", "reason": "광대한 세계와 깊은 스토리의 JRPG 명작"},
        {"title": "Elden Ring", "reason": "도전과 탐험의 재미가 극대화된 오픈월드 RPG"},
    ],
    ("전략", "1시간 미만", "PC"): [
        {"title": "Into the Breach", "reason": "짧은 턴 수로 완결되는 퍼즐형 전략 게임"},
        {"title": "Slay the Spire", "reason": "런당 1시간 내외, 중독성 있는 덱빌딩 전략"},
    ],
    ("전략", "1~3시간", "PC"): [
        {"title": "Civilization VI", "reason": "한 판 한 판 깊이 있는 문명 건설 전략"},
        {"title": "XCOM 2", "reason": "긴장감 넘치는 턴제 전술 전략 게임"},
    ],
    ("전략", "3시간 이상", "PC"): [
        {"title": "Total War: Warhammer III", "reason": "대규모 전투와 캠페인이 결합된 전략의 끝판왕"},
        {"title": "Crusader Kings III", "reason": "중세 왕조 시뮬레이션, 무한한 스토리 생성"},
    ],
    ("스포츠", "1시간 미만", "PC"): [
        {"title": "Rocket League", "reason": "5분 경기로 빠르게 즐길 수 있는 차량 축구 게임"},
        {"title": "FIFA Online 4", "reason": "한 경기 단위로 즐기기 좋은 축구 게임"},
    ],
    ("스포츠", "1시간 미만", "콘솔"): [
        {"title": "EA Sports FC 25", "reason": "짧은 경기 단위로 언제든 즐길 수 있는 축구 게임"},
        {"title": "NBA 2K25", "reason": "쿼터 단위로 짧게 즐기기 좋은 농구 게임"},
    ],
    ("스포츠", "1~3시간", "PC"): [
        {"title": "Football Manager 2024", "reason": "감독이 되어 팀을 운영하는 깊이 있는 축구 시뮬"},
        {"title": "MLB The Show 24", "reason": "야구의 깊은 재미를 PC에서 경험"},
    ],
    ("스포츠", "1~3시간", "콘솔"): [
        {"title": "MLB The Show 24", "reason": "실감 나는 야구 시뮬레이션의 콘솔 최강자"},
        {"title": "Tony Hawk's Pro Skater 1+2", "reason": "스테이지 단위로 즐기는 스케이트보드 게임"},
    ],
}

def get_recommendation(genre: str, play_time: str, platform: str):
    key = (genre, play_time, platform)
    games = GAME_DB.get(key)

    if games:
        return games

    # 완전히 일치하는 키가 없으면 장르만 맞는 것 중 랜덤 반환
    fallback = []
    for k, v in GAME_DB.items():
        if k[0] == genre:
            fallback.extend(v)

    if fallback:
        return fallback[:2]

    return [
        {"title": "Minecraft", "reason": "어떤 취향에도 맞는 자유도 높은 샌드박스 게임"},
        {"title": "Stardew Valley", "reason": "힐링과 성취감을 동시에 주는 인디 명작"},
    ]

@app.get("/")
def root():
    return {"message": "Game Recommendation API is running!"}

@app.post("/recommend")
def recommend(req: GameRequest):
    games = get_recommendation(req.genre, req.play_time, req.platform)
    return {
        "input": {
            "genre": req.genre,
            "play_time": req.play_time,
            "platform": req.platform,
        },
        "recommendations": games
    }
