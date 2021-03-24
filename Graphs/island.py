# Write a function that takes a 2D binary array and returns the number of 1 islands. 
# An island consists of 1s that are connected to the north, south, east or west. For example:

class Stack:
    def __init__(self):
        self.storage = []
    
    def push(self, value):
        self.storage.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None

    def size(self):
        return len(self.storage)

class Queue():
    def __init__(self):
        self.storage = []
    def enqueue(self, value):
        self.storage.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None
    def size(self):
        return len(self.storage)

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]


def get_neighbors(row, col, island_matrix):
    neighbors = []

    # check north.
    if row > 0 and island_matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))

    # check south
    if row < len(island_matrix) - 1 and island_matrix[row + 1][col] == 1:
         neighbors.append((row + 1, col))

    # check east
    if col < len(island_matrix[0]) - 1 and island_matrix[row][col + 1] == 1:
         neighbors.append((row, col + 1))

    # check west.
    if col > 0 and island_matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
   
    return neighbors

def dft(row, col, island_matrix, visited_matrix):
    # create an empty stack
    s = Stack()

    # push starting vertex on to the stack (col, row)
    s.push((row, col))

    # while the stack is not empty
    while s.size() > 0:
        # pop the vertex off the Stack
        v = s.pop()
        # extract the row and col
        row = v[0]
        col = v[1]

        # if the current element is not in visited
        if not visited_matrix[row][col]:
            # set the element to visited
            visited_matrix[row][col] = True

            # iterate over the neighbors:
            for neighbor in get_neighbors(row, col, island_matrix):
                # push the neighbor on to the stack
                s.push(neighbor)
    
    # return the visited matrix to the caller
    return visited_matrix

def bft(row, col, island_matrix, visited_matrix):
    # create an empty queue
    q = Queue()

    # push starting vertex on to the queue (row, col)
    q.enqueue((row, col))

    # while the queue is not empty
    while q.size() > 0:
        # dequeue the vertex off the Stack
        v = q.dequeue()
        # extract the row and col
        row = v[0]
        col = v[1]

        # if the current element is not in visited
        if not visited_matrix[row][col]:
            # set the element to visited
            visited_matrix[row][col] = True

            # iterate over the neighbors:
            for neighbor in get_neighbors(row, col, island_matrix):
                # enqueue the neighbor on to the stack
                q.enqueue(neighbor)
    
    # return the visited matrix to the caller
    return visited_matrix




def island_counter(islands):
    # create a visited matrix (2d list)
    visited = []
    # initialize the visited matrix with False's
    for i in range(len(islands)):
        visited.append([False] * len(islands[0]))

    # initialize an island_counte to zero
    island_count = 0

    # walk through the matrix via a nested foor loop
    # col
    for col in range(len(islands[0])):
        # row
        for row in range(len(islands)):
            # check if matrix at current row and col are in visited
            if not visited[row][col]:
                # check if current element is a 1
                if islands[row][col] == 1:

                    # do a dft on the island_matrix returning a updated copy of the visited matrix
                    visited = dft(row, col, islands, visited)
                    # increment the island_count
                    island_count += 1
                else:
                    visited[row][col] = True

    return island_count



print(island_counter(islands)) # returns 4