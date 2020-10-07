def recursive_function(n):
    if n == 100:
        return
    print(n, "번째 재귀함수에서", n+1, "번째 재귀함수를 호출합니다.")
    recursive_function(n+1)
    print(n, "번째 재귀함수가 종료됩니다.")


recursive_function(1)
