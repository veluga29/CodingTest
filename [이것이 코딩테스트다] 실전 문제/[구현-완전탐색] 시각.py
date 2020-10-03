# 내 풀이
n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 3이 포함된 시각이 있으면 count한다.
            # 지향할 테크닉 : if '3' in str(i) + str(j) + str(k)
            if '3' in str(i) or '3' in str(j) or '3' in str(k):
                count += 1

print(count)
