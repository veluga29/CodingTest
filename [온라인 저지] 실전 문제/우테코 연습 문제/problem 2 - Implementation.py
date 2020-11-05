# 내 풀이
def solution(word):
    result = ""

    # 단어를 한 글자 씩 처리
    for w in word:
        if w.isupper():  # 글자가 대문자일 경우
            result += chr((ord('Z') - (ord(w) - ord('A'))))  # 아스키 코드로 변환 계산해 문자열에 추가
        elif w.islower():  # 글자가 소문자일 경우
            result += chr((ord('z') - (ord(w) - ord('a'))))
        else:  # 알파벳 이외의 글자(공백)일 경우
            result += w  # 문자열 그냥 추가

    return result


print(solution("I love you"))
