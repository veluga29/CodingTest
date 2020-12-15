array = [3, 5, 0, 2, 2, 3, 4, 4, 4, 5, 1, 0]
n = len(array)

# 모든 원소에 대하여 두 개씩 비교해 오름차순 정렬
for itr1 in range(n):
    for itr2 in range(itr1 + 1, n):
        # 두 원소 중 앞의 원소가 크다면, 서로 위치를 바꿈 (오름차순 정렬)
        if array[itr1] > array[itr2]:
            array[itr1], array[itr2] = array[itr2], array[itr1]

print(array)
