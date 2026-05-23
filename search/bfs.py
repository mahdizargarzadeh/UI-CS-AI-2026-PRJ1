from collections import deque

def bfs(start):

    if start.is_goal_state():
        return []

    q = deque()
    q.append((start, []))
    visited = set()
    visited.add(start)

    while q:
        state, path = q.popleft()

        for action, cost, next_state in state.get_successors():

            if next_state.is_collision_state():
                continue

            if next_state.is_goal_state():
                return path + [action]

            if next_state not in visited:
                visited.add(next_state)
                q.append((next_state, path + [action]))

    return []
