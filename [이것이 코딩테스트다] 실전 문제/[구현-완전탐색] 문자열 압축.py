# 내 풀이 - 문제 풀이 실패, 답안 아이디어는 근접


def solution(s):
    answer = len(s)

    # 1개 단위부터 압축 단위를 늘려가며 확인
    for i in range(1, len(s) // 2 + 1):
        head = s[0:i]  # 해당 압축 단위만큼 앞에서부터 문자열 추출
        compressed = ""
        count = 1

        # 해당 압축 단위만큼 증가시키며 head 문자열과 비교
        for j in range(i, len(s), i):
            # head 문자열과 동일하다면 압축 횟수 증가
            if head == s[j:j + i]:
                count += 1
            # 다른 문자열이라면
            else:
                compressed += str(count) + head if count >= 2 else head  # 이전까지의 결과를 압축
                head = s[j:j + i]  # 다시 상태 초기화
                count = 1
                # 남아 있는 문자열 처리
        compressed += str(count) + head if count >= 2 else head
        # 가장 짧은 압축 문자열 선택
        answer = min(answer, len(compressed))

    return answer
