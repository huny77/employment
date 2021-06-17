import copy
import sys

sys.setrecursionlimit(100000)


def solution(land, height):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = len(land)
    edges = [[0] * n for _ in range(n)]
    visited = copy.deepcopy(edges)

    # 대륙 만들기
    def dfs(y, x, land_num):
        if edges[y][x] != 0:
            return False
        edges[y][x] = land_num
        for (dy, dx) in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and abs(land[y][x] - land[ny][nx]) <= height:
                dfs(ny, nx, land_num)
        return True

    land_number = 1

    # 각각의 대륙을 만듬
    for y in range(n):
        for x in range(n):
            if dfs(y, x, land_number):
                land_number += 1

    # 대륙간의 길이 구하기
    def dfs2(y, x):
        if visited[y][x] != 0:
            return
        visited[y][x] = True
        for (dy, dx) in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and edges[y][x] != edges[ny][nx]:
                edges.append((abs(land[y][x] - land[ny][nx]), edges[y][x], edges[ny][nx]))
        return True

    # 각각 대륙끼리의 최소 거리를 구함
    edges = []
    for y in range(n):
        for x in range(n):
            dfs2(y, x)
    edges.sort()

    # MST
    data = {key: key for key in range(land_number)}
    rank = {key: 1 for key in range(land_number)}

    def find(node: int) -> int:
        if data[node] != node:
            data[node] = find(data[node])
        return data[node]

    def union(a: int, b: int) -> None:
        root1 = find(a)
        root2 = find(b)

        if root1 == root2:
            return

        if rank[root1] > rank[root2]:
            root1, root2 = root2, root1

        data[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

    cnt = 0
    weight = 0

    for (cost, a, b) in edges:
        if find(a) != find(b):
            union(a, b)
            cnt += 1
            weight += cost
            if cnt == land_number - 2:
                break

    return weight
