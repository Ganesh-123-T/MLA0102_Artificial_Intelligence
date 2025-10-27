from queue import Queue

goal = [[1,2,3],[4,5,6],[7,8,0]]
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def is_goal(state):
    return state == goal

def to_tuple(state):
    return tuple(map(tuple, state))

def bfs(start):
    q = Queue()
    q.put(start)
    visited = {to_tuple(start): None}
    while not q.empty():
        state = q.get()
        if is_goal(state):
            return state
        x, y = find_zero(state)
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                t = to_tuple(new_state)
                if t not in visited:
                    visited[t] = state
                    q.put(new_state)

start = [[1,2,3],[4,0,6],[7,5,8]]
result = bfs(start)
print("Final Solved State:")
for row in result:
    print(row)
