def solution(relations, t):
    firstFree = -1

    for i in range(0, len(t)):
        if not t[i]:
            firstFree = i
            break
    if firstFree == -1:
        return 1

    result = 0
    for pair in range(firstFree + 1, len(t)):
        if not t[pair] and relations[firstFree][pair]:
            t[firstFree] = t[pair] = True
            result += solution(relations, t)
            t[firstFree] = t[pair] = False
    return result


count = int(input())
res = []
for c in range(0, count):
    N, L = map(int, input().split())
    r = list(map(int, input().split()))
    areFriend = [[False for j in range(0, N)] for i in range(0, N)]
    taken = [False for i in range(0, N)]
    idx = 0
    while idx < L * 2:
        areFriend[r[idx]][r[idx + 1]] = True
        areFriend[r[idx + 1]][r[idx]] = True
        idx += 2
    print(solution(areFriend, taken))
