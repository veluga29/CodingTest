def solution(tickets):
    tickets.sort(reverse=True)

    graph = dict()
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    stack = ['ICN']
    answer = []

    while stack:
        if stack[-1] not in graph or len(graph[stack[-1]]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[stack[-1]].pop())

    return answer[::-1]


# def dfs(start, tickets, result):
#     if len(tickets) == 0:ㄱ
#         return result
#     for i,ticket in enumerate(tickets):
#         if start == ticket[0]:
#             end = ticket[1]
#             tickets.pop(i)
#             result.append(end)
#             temp = dfs(end,tickets, result)
#             if len(temp)!=0:
#                 return temp
#             result.pop(len(result)-1)
#             tickets.insert(i,[start,end])
#
#     return []
#
# def solution(tickets):
#     tickets.sort()
#     result = []
#     start = "ICN"
#     result.append(start)
#     answer = dfs(start, tickets, result)
#
#     return answer
