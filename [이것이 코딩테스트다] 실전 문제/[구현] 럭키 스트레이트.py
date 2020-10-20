# 내 풀이

n = list(map(int, input()))

pivot = len(n) // 2

left = sum(n[0:pivot])
right = sum(n[pivot:])

if left == right:
    print("LUCKY")
else:
    print("READY")
