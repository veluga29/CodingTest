# 주목할 점:
# 1. 인덱싱할 요소가 없는 경우를 고려해야할 때, 슬라이싱을 활용하면 오류 없이 동작시킬 수 있다.
# 2. enumerate를 루핑할 때 for문 변수에 언패킹할 요소가 (인덱스, 튜플)이라면, ()를 사용해 언패킹을 용이하게 할 수 있다.
# 예시) for i, (genre, play) in enumerate(zip(genres, plays)):
#
# 시간 복잡도:
# 최악의 경우 O(Nlog(N)) 보장 - 장르에 속한 곡들을 정렬할 때
# 일반적인 경우 O(N) - 딕셔너리를 목적대로 분류할 때


# 내 풀이
# from collections import defaultdict
#
#
# def solution(genres, plays):
#     answer = []
#     # 장르 별 플레이 수와 장르 별 노래 목록을 담을 두 개의 딕셔너리 생성
#     plays_by_genre = defaultdict(int)
#     songs_by_genre = defaultdict(list)
#
#     # 각 딕셔너리를 목적대로 분류
#     for i, gp in enumerate(zip(genres, plays)):
#         genre, play = gp
#         plays_by_genre[genre] += play
#         songs_by_genre[genre].append((play, i))
#
#     # 가장 플레이 수가 많은 장르부터 차례로
#     for i in sorted(plays_by_genre.items(), key=lambda x: x[1], reverse=True):
#         # 플레이 수가 가장 많은 순서대로 해당 장르의 곡들을 정렬
#         songs_by_genre[i[0]].sort(key=lambda x: x[0], reverse=True)
#         # 첫 번째 곡을 베스트 앨범에 삽입
#         answer.append(songs_by_genre[i[0]][0][1])
#         # 장르에 곡이 두 개 이상이라면
#         if len(songs_by_genre[i[0]]) > 1:
#             # 두 번째 곡을 베스트 앨범에 삽입
#             answer.append(songs_by_genre[i[0]][1][1])
#
#     return answer


# 수정한 풀이
from collections import defaultdict


def solution(genres, plays):
    answer = []
    # 장르 별 플레이 수와 장르 별 노래 목록을 담을 두 개의 딕셔너리 생성
    plays_by_genre = defaultdict(int)
    songs_by_genre = defaultdict(list)

    # 각 딕셔너리를 목적대로 분류
    for i, (genre, play) in enumerate(zip(genres, plays)):
        plays_by_genre[genre] += play
        songs_by_genre[genre].append((play, i))

    # 가장 플레이 수가 많은 장르부터 차례대로
    for i in sorted(plays_by_genre.items(), key=lambda x: x[1], reverse=True):
        # 해당 장르에서 플레이 수가 가장 많은 곡들을 최대 두 곡까지 베스트 앨범에 삽입
        for j in sorted(songs_by_genre[i[0]], key=lambda x: x[0], reverse=True)[0:2]:
            answer.append(j[1])

    return answer
