# 관계식을 구해 이차방정식으로 정리한 다음 근의 공식 사용
def solution(brown, yellow):
    term = (((brown + 4) / 2) ** 2 - 4 * (brown + yellow)) ** 0.5
    w = ((brown + 4) / 2 + term) / 2
    h = ((brown + 4) / 2 - term) / 2
    return [w,h]