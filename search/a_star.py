def a_star():
    pass
def a_star(initial_state):
    def heuristic (*args):
        pass


def heuristic_func(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def MST(nodes):

    V_tree = {nodes[0]}
    V_not_tree = set(nodes[1:])
    edge_cost = {}

    for node in V_not_tree:
        edge_cost[node] = heuristic_func(nodes[0], node)
        
    total_cost = 0
    while V_not_tree:

        min = float('inf')
        for node in V_not_tree:
            if edge_cost[node] < min:
                min = edge_cost[node]
                selected = node

        V_tree.add(selected)
        V_not_tree.remove(selected)
        total_cost += edge_cost[selected]

        for n in V_not_tree:
            d = heuristic_func(selected, n)
            if d < edge_cost[n]:
                edge_cost[n] = d

    return total_cost