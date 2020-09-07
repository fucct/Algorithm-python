def solve(path, dist, visited, currentDist):
    length = len(visited)

    if len(path) == length:
        return currentDist + dist[path[-1]][path[0]]

    ret = 1416 * length
    for idx in range(0, length):
        if not visited[idx]:
            here = path[-1]
            nextIdx = idx
            path.append(nextIdx)
            visited[nextIdx] = True
            ret = min(ret, solve(path, dist, visited, currentDist + dist[here][nextIdx]))
            path.remove(nextIdx)
            visited[nextIdx] = False
    return ret


count = int(input())
for c in range(0, count):
    n = int(input())

    dist = []
    path = [0]
    visited = [True, *[False for a in range(1, n)]]
    currentDist = 0.0
    for i in range(0, n):
        dist.append(list(map(float, input().split())))
    print(solve(path, dist, visited, currentDist))
