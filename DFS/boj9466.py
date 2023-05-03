import sys

# cycle = team
def dfs(num):
    global result
    stack = [num]
    while True:
        now = stack[-1]
        visit[now] = True
        next = lst[now -1]
        if not visit[next]:
            stack.append(next)
        else:
            # cycle이 존재하는 경우(이전에 방문을 한 지점)
            if next in stack:
                idx = stack.index(next)
                # cycle에 존재하는 팀원의 수
                result += len(stack[idx:])
            break
    return

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    result = 0
    lst = list(map(int, sys.stdin.readline().split()))
    visit = [False] * (n+1)
    for i in range(n):
        if not visit[i+1]:
            dfs(i+1)
    print(n - result)
