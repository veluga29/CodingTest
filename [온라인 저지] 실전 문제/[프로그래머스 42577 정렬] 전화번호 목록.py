# 내 풀이 - 시간 복잡도 O(N²)
# 문제점: 단순 비교로 인해, 시간 복잡도가 크다.
# 해결책: 정렬하면 인접한 노드들만 확인하면 된다. 아이디어 하나로 시간 복잡도가 크게 줄어든다.


def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            min_len = min(len(phone_book[i]), len(phone_book[j]))
            if phone_book[j][:min_len] == phone_book[i][:min_len]:
                return False
    return True

# 모범 답안 - 시간 복잡도 O(NlogN)
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True
