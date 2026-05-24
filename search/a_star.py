import heapq

def a_star(initial_state):
    
    def heuristic(state):
        agent = state.get_agent_position()
        targets = list(state.get_targets_positions())

        if len(targets) == 0:
            return 0            
        
        closest_cost = min(heuristic_func(agent, t) for t in targets)

        if len(targets) == 1:
            mst_cost = 0
        else:
            mst_cost = (MST(targets))

        cost = (closest_cost + mst_cost) * 5                       

        return cost

    if initial_state.is_goal_state():
        return []
    
    expand_time = 0
    frontier = [(heuristic(initial_state), expand_time, 0, initial_state, [])]
    reached = {initial_state : 0}

    while frontier:

        f_n, time, g_n, state, path = heapq.heappop(frontier)
        
        if state.is_goal_state():
            return path
        
        if g_n > reached[state]:
            continue

        for action, step_cost, next_state in state.get_successors():

            if next_state.is_collision_state():
                continue

            g_child = g_n + step_cost
            if next_state not in reached or g_child < reached[next_state]:

                reached[next_state] = g_child
                f_n = g_child + heuristic(next_state)
                expand_time += 1
                heapq.heappush(frontier, (f_n, expand_time, g_child, next_state, path + [action]))

    return []



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