from collections import deque

def bfs(initial_state):

    if initial_state.is_goal_state():
        return []

    node_queue = deque()
    node_queue.append((initial_state, []))
    visited = set()
    visited.add(initial_state)

    while node_queue:
        state, path = node_queue.popleft()

        for action, cost, next_state in state.get_successors():

            if next_state.is_collision_state():
                continue

            if next_state.is_goal_state():
                return path + [action]

            if next_state not in visited:
                visited.add(next_state)
                node_queue.append((next_state, path + [action]))

    return []
