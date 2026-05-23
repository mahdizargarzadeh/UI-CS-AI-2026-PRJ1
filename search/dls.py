def dls(start_node, max_d=120):
    if start_node.is_goal_state():
        return []

    for d in range(1, max_d + 1):
        checked_nodes = {}
        checked_nodes[start_node] = d
        final = search_helper(start_node, [], d, checked_nodes)
        if final != False:
            return final 
            
    return []

def search_helper(state, current, depth, checked):
    if state.is_goal_state():
        return current
        
    if depth == 0:
        return False
        
    successors = state.get_successors()
    for i in range(len(successors)):
        action = successors[i][0]
        cost = successors[i][1]
        nextstate = successors[i][2]
        skip = False
        
        if nextstate.is_collision_state():
            continue
            
        if nextstate in checked:
            if checked[nextstate] >= (depth - 1):
                skip = True
                
        if skip == False:
            checked[nextstate] = depth - 1
            newpath = current.copy()
            newpath.append(action)
            ret = search_helper(nextstate, newpath, depth - 1, checked)
            if ret != False:
                return ret
                
    return False