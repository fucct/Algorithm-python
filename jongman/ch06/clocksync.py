switches = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]


def solve(clocks, s):
    if s == 10:
        for clock in clocks:
            if clock != 12:
                return 31
        return 0

    ret = 50
    for i in range(0, 4):
        ret = min(ret, i + solve(clocks, s + 1))
        for j in range(0, len(switches[s])):
            clocks[switches[s][j]] += 3
            if clocks[switches[s][j]] == 15:
                clocks[switches[s][j]] = 3
    if ret == 50:
        return -1
    return ret


count = int(input())
for c in range(0, count):
    clocks = list(map(int, input().split()))
    print(solve(clocks, 0))
