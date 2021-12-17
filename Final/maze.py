import random
import sys
import heapq as hq
import math
from time import process_time_ns

EMPTY = ' '
WALL = '#'
AGENT = 'o'
GOAL = 'x'
MOVED = '@'

def adjacent(cell):
  i,j = cell
  for (y,x) in ((1,0), (0,1), (-1, 0), (0,-1)):
    yield (i+y, j+x), (i+2*y, j+2*x)

def generate(width, height, verbose=True):
  '''Generates a maze as a list of strings.
     :param width: the width of the maze, not including border walls.
     :param heihgt: height of the maze, not including border walls.
  '''
  # add 2 for border walls.

  width += 2 
  height += 2
  rows, cols = height, width

  maze = {}

  spaceCells = set()
  connected = set()
  walls = set()

  # Initialize with grid.
  for i in range(rows):
    for j in range(cols):
      if (i%2 == 1) and (j%2 == 1):
        maze[(i,j)] = EMPTY
      else:
        maze[(i,j)] = WALL 

  # Fill in border.
  for i in range(rows):
    maze[(i,0)] = WALL
    maze[(i,cols-1)] = WALL
  for j in range(cols):
    maze[(0,j)] = WALL
    maze[(rows-1,j)] = WALL

  for i in range(rows):
    for j in range(cols):
      if maze[(i,j)] == EMPTY:
        spaceCells.add((i,j))
      if maze[(i,j)] == WALL:
        walls.add((i,j))

  # Prim's algorithm to knock down walls.
  originalSize = len(spaceCells)
  connected.add((1,1))
  while len(connected) < len(spaceCells):
    doA, doB = None, None
    cns = list(connected)
    random.shuffle(cns)
    for (i,j) in cns:
      if doA is not None: break
      for A, B in adjacent((i,j)):
        if A not in walls: 
          continue
        if (B not in spaceCells) or (B in connected):
          continue
        doA, doB = A, B
        break
    A, B = doA, doB
    maze[A] = EMPTY
    walls.remove(A)
    spaceCells.add(A)
    connected.add(A)
    connected.add(B)
    if verbose:
      cs, ss = len(connected), len(spaceCells)
      cs += (originalSize - ss)
      ss += (originalSize - ss)
      if cs % 10 == 1:
        print('%s/%s cells connected ...' % (cs, ss), file=sys.stderr)

  # Insert character and goals.
  TL = (1,1)
  BR = (rows-2, cols-2)
  if rows % 2 == 0:
    BR = (BR[0]-1, BR[1])
  if cols % 2 == 0:
    BR = (BR[0], BR[1]-1)

  maze[TL] = AGENT
  maze[BR] = GOAL

  lines = []
  for i in range(rows):
    lines.append(''.join(maze[(i,j)] for j in range(cols)))

  return lines

#######################################################################################################
# Manhattan distance heuristic
def h(u,v):
   return abs(u[1]-v[1])+abs(u[0]-v[0])

# Misc functions for list conversions
def ls_ll(G):
    Gcopy = []
    for i in G:
      Gcopy.append(list(i))
    return Gcopy
  
def ll_ls(maze):
    maze_copy = []
    for i in maze:
      maze_copy.append(''.join(i))
    return maze_copy
    
def dijkstra(maze):
    # initialization
    maze_copy = ls_ll(maze)
    n = len(maze)#row
    m = len(maze[0])#column
  
    visited = [False]*m*n
    weights = [math.inf]*m*n
    queue = []
    adj = [[0,1],[1,0],[-1,0],[0,-1]]

    # Finding start
    # busca al agente la ubicacion de el agente, en la pocicion de el agente se le asigna 0 en weight
    agent_location = [0,0]
    for y in range(n):
      for x in range(m):
        if maze[y][x] == AGENT:
          agent_location[1] = x
          agent_location[0] = y
    weights[agent_location[0]*m+agent_location[1]] = 0 #posicion 12 tiene valor a 0
    hq.heappush(queue, (0, agent_location)) 
    
    while len(queue) > 0:
      
        weight, position = hq.heappop(queue)
        
        weights[y*m+x] = weight #goal weigth[120] = 0 end
        visited[position[0]*m+position[1]] = True #agent visited true
        maze_copy[position[0]][position[1]] = MOVED #change agent to @
        # Printing each iteration
        print('\n'.join(ll_ls(maze_copy)), '\n')

        if maze[position[0]][position[1]] == GOAL:
          # Printing Final
          print('FINAL\n','\n'.join(ll_ls(maze_copy)), '\n')
          return 'distance of goal is = '+ str(weight), weights
        
        
        #visiting neigbors
        for v in adj:
          y = position[0]+v[0]
          x = position[1]+v[1]
          
          #less than the borders, not visited, not a wall 
          if y>=0 and y<n and x>=0 and x<m and maze[y][x] != WALL and visited[y*m+x]==False:
            f = weight + 1 # increment weight by
            hq.heappush(queue, (f, [y,x]))
            
    return 'Not found', weights

def Astar(maze):
    #initialization
    maze_copy = ls_ll(maze)
    n = len(maze)
    m = len(maze[0])
    visited = [False]*m*n
    weights = [math.inf]*m*n
    queue = []
    adj = [[0,1],[1,0],[-1,0],[0,-1]]

    # finding start
    u = [0,0]
    for y_ in range(n):
      for x_ in range(m):
        if maze[y_][x_] == AGENT:
          u[1] = x_
          u[0] = y_
    weights[u[0]*m+u[1]] = 0
    hq.heappush(queue, (0, u))

    # finding Goal
    V = [0,0]
    for y_ in range(n):
      for x_ in range(m):
        if maze[y_][x_] == GOAL:
          V[1] = x_
          V[0] = y_
    
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        weights[y_*m+x_] = g
        visited[u[0]*m+u[1]] = True
        maze_copy[u[0]][u[1]] = MOVED
        # Printing each iteration
        print('Next iteration\n','\n'.join(ll_ls(maze_copy)), '\n')

        if maze[u[0]][u[1]] == GOAL:
          # Printing Final
          print('FINAL\n','\n'.join(ll_ls(maze_copy)), '\n')
          return 'distance of goal is = '+ str(g), weights
        for v in adj:
            y_ = u[0]+v[0]
            x_ = u[1]+v[1]
            u_ = [y_,x_]
            if y_>=0 and y_<n and x_>=0 and x_<m and maze[y_][x_] != WALL and visited[y_*m+x_]==False:
              f = g + 1 + h(u_,V)
              hq.heappush(queue, (f, [y_,x_]))
    return 'Not found', weights
  
  ###################################################################################################################

if __name__ == '__main__':
  width = 9
  height = 9

  args = sys.argv[1:]
  if len(args) >= 1:
    width = int(args[0])
  if len(args) >= 2:
    height = int(args[1])

  if len(args) < 2:
    print('Use command-line args to specify width and height.', file=sys.stderr)
    print('  Odd numbers are suggested because of the walls.', file=sys.stderr)
  print('Non-maze text is printed to stderr, so you \n  can use > to pipe just the maze to a file.\n', file=sys.stderr)

  print('Generating %sx%s maze (not including border)...\n' % (width, height), file=sys.stderr)

  maze = generate(width, height)
  print('Done.\n', file=sys.stderr)
  print('\n'.join(maze))



  print('\nFinding distance using Dijkstra\n')
  enter_pause = input()
  t1_start = process_time_ns()
  dijkstra(maze);
  t1_stop = process_time_ns()
  print("\nTime Taken (Dijkstra): \n ", (t1_stop-t1_start)/1000000000, "Secs")


  enter_pause = input()

  print('\nFinding distance using A* (Manhattan)\n ')
  enter_pause = input()
  t2_start = process_time_ns()
  Astar(maze);
  t2_stop = process_time_ns()
  print("\nTime Taken (A*):\n ", (t2_stop-t2_start)/1000000000, "Secs")