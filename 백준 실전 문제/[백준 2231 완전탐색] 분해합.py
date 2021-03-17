# 내 풀이
# 시간 복잡도: O(N)

n = int(input())
result = 0

# n보다 작은 모든 수에 대하여
for i in range(n):
    # 분해합 구하기
    cnt = len(str(i))
    div_sum = i
    for j in range(cnt):
        div_sum += int(str(i)[j])
    # 만일 i가 n의 생성자라면 i를 저장하고 반복문 종료
    if div_sum == n:
        result = i
        break

# 결과 출력
print(result)
