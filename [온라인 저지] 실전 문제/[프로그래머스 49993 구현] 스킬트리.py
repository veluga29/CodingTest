# 내 풀이
def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skill_count = 0  # 선행 스킬 순서 중 현재 배울 수 있는 스킬의 인덱스
        tree_possible = True  # 스킬 트리 가능성 여부
        for s in tree:
            if s not in skill:  # 해당 스킬이 선행 스킬 순서에 없다면, 바로 배움
                continue
            # 해당 스킬이 선행 스킬 순서에 있다면
            if s == skill[skill_count]:  # 지금 배울 수 있다면 배움
                skill_count += 1
            else:  # 선행 스킬이 없다면, 배울 수 없는 스킬트리로 간주
                tree_possible = False
                break
        if tree_possible:
            answer += 1

    return answer
