# 내 풀이
def solution(cryptogram):
    crypt_list = list(cryptogram)  # 문자열을 한 글자씩 리스트에 담음
    pop_flag = False  # 중복 제거가 실행됨을 알리는 표시

    while True:
        rep_flag = False  # 한 번이라도 중복이 있었음을 알리는 표시
        # crypt_list를 뒤에서부터 두 글자씩 비교함
        for i in range(len(crypt_list) - 1, 0, -1):
            if pop_flag:  # 이전 단계에 중복제거가 한 번 실행됐었다면
                pop_flag = False
                continue  # 이번 글자는 중복 체크를 생략
            # i 번째 글자가 i - 1 번째 글자와 같다면, 중복 제거 수행
            if crypt_list[i] == crypt_list[i - 1] :
                crypt_list.pop(i)
                crypt_list.pop(i - 1)
                pop_flag = True
                rep_flag = True
        # 한 번도 중복된 글자가 없었다면, 반복문 중지
        if not rep_flag:
            break

    return ''.join(crypt_list)


print(solution("browoanoommnaon"))
print(solution("zyelleyz"))
print(solution("b"))
