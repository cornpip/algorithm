import sys
T = int(input())

# node index 0부터임
def dfs(node_graph, now_node, path, cost: list):
    race = []
    # print(node_graph[now_node])
    for next_node in node_graph[now_node]:
        # print(next_node)
        x_weight = cost[0]+weight_graph[now_node][next_node][0]
        y_weight = cost[1]+weight_graph[now_node][next_node][1]
        n_cost = [x_weight, y_weight]
        if next_node == 1:
            race.append(n_cost[0] * n_cost[1])
            continue
        if next_node in path:
            continue
        path.append(next_node)
        res = dfs(node_graph, next_node, path, n_cost)
        if res:
            race.append(res)
    # print(race, now_node)
    if not race:
        return None
    return min(race)

for case in range(T):
    try:
        n, m = map(int, input().split())
    except:
        continue
    node_graph = [[] for _ in range(n)] # index 0부터
    weight_graph = [[[0,0] for _ in range(n) ] for i in range(n)]
    for edge in range(m):
        a, b, x, y = map(int, input().split())
        a, b = a-1, b-1
        node_graph[a].append(b)
        node_graph[b].append(a)
        weight_graph[a][b][0], weight_graph[a][b][1] = x, y
        weight_graph[b][a][0], weight_graph[b][a][1] = x, y
    # print(weight_graph)
    ans = dfs(node_graph, 0, [0], [0,0])
    if not ans:
        ans = -1
    print(f"#{case+1} {ans}")