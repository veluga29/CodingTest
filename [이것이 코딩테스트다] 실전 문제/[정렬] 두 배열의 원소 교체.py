n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 배열 A를 오름차순 정렬
b.sort(reverse=True)  # 배열 B를 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 최대 K번 두 배열의 원소를 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 원소 교환
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같을 경우, 반복문 탈출
    else:
        break

result = sum(a)
print(result)
