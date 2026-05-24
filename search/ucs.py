import heapq

def ucs(start):
  if start.is_goal_state() == True:
      return []
  counter = 0
  queue = []
  heapq.heappush(queue, (0, counter, start, []))
  costs = {}
  costs[start] = 0
  
  while len(queue) > 0:
      current = heapq.heappop(queue)
      cost = current[0]
      state = current[2]
      path = current[3]
      if cost > costs[state]:
          continue
      if state.is_goal_state() == True:
          return path
          
      for action, stepcost, nextstate in state.get_successors():
          if nextstate.is_collision_state() == True:
              continue
          newcost = cost + stepcost
          if nextstate in costs:
              oldcost = costs[nextstate]
          else:
              oldcost = float('inf')
          if newcost < oldcost:
              costs[nextstate] = newcost
              counter = counter + 1
              newpath = path + [action]
              heapq.heappush(queue, (newcost, counter, nextstate, newpath))
  return []
     
