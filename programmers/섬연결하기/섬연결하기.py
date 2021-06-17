def solution(n: int, costs: list) -> int:
    data = {key: key for key in range(n + 1)}
    rank = {key: 1 for key in range(n + 1)}

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

    def find(node: int) -> int:
        if data[node] != node:
            data[node] = find(data[node])
        return data[node]

    costs.sort(key=lambda x: x[2])
    weight = 0
    cnt = 0

    for s, e, c in costs:
        if find(s) != find(e):
            union(s, e)
            weight += c
            cnt += 1
            if cnt == n + 1:
                return weight

    return weight
