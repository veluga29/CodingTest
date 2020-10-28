# 내 풀이
n = int(input())

info = []
for i in range(n):
    input_data = input().split()
    info.append((input_data[0], int(input_data[1])))  # 이름은 문자열로, 성적은 정수로 저장

# 점수를 기준으로 오름차순 정렬
info.sort(key=lambda x: x[1])

for i in info:
    print(i[0], end=' ')
