# 내 풀이
n = int(input())
words = []
# 단어들을 입력 받아 리스트에 삽입
for _ in range(n):
    words.append(input())

# 중복되는 단어 제거
words = list(set(words))
# 조건에 맞춰 정렬 수행
words.sort(key=lambda x: (len(x), x))

# 결과 출력
for word in words:
    print(word)
