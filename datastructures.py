class Node:
    # Constructor for Node, representing each cell on the Minesweeper board
    def __init__(self, x, y, value='cover'):    # Average: O(1), Worst: O(1)
        self.x = x  
        self.y = y  
        self.value = value  # Value of the node, initially set to 'cover'
        self.adjacent = []  # List to store adjacent nodes

    # Adds an adjacent node to the current node
    def add_adjacent(self, node):   # Average: O(1), Worst: O(1)
        self.adjacent.append(node)  # Appending the adjacent node
        # This method establishes connections between adjacent cells


class Graph:
    # Constructor for Graph, representing the logical structure of the Minesweeper board
    def __init__(self, size):    # Average: O(n^2), Worst: O(n^2)
        self.size = size  # Size of the board
        # Creating a 2D grid of nodes
        self.nodes = [[Node(x, y) for y in range(size)] for x in range(size)]

        # Establishing adjacency relations for each node
        for x in range(size):
            for y in range(size):
                node = self.nodes[x][y]
                # Checking all possible adjacent positions
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue  # Skip the current node
                        nx, ny = x + dx, y + dy  # Calculating adjacent coordinates
                        # Check if adjacent position is within the board
                        if 0 <= nx < size and 0 <= ny < size:
                            adj_node = self.nodes[nx][ny]
                            if adj_node not in node.adjacent:
                                node.add_adjacent(adj_node)  # Add adjacent node
        # The Graph data structure effectively models the Minesweeper board as a network of nodes,

    # Retrieves a node from the board given its coordinates
    def get_node(self, x, y):   # Average: O(1), Worst: O(1)
        return self.nodes[x][y] 
        # This method provides quick access to any cell on the board
