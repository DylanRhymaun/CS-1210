"""
BFS
Dylan Rhymaun

"""

ROUTES = {
        'Burlington': ['St Albans', 'Montpelier', 'Middlebury'],
        'Montpelier': ['Burlington', 'White River Junction', 'St Johnsbury'],
        'White River Junction': ['Montpelier', 'Brattleboro', 'St Johnsbury'],
        'Brattleboro': ['White River Junction'],
        'Newport': ['St Johnsbury'],
        'St Albans': ['Burlington', 'Swanton'],
        'St Johnsbury': ['Montpelier', 'White River Junction', 'Newport'],
        'Swanton': ['St Albans'],
        'Middlebury': ['Burlington', 'Rutland'],
        'Rutland': ['Middlebury', 'Bennington'],
        'Bennington': ['Rutland']
}

def bfs(adj_list, start):
    try:
        neighbors = adj_list[start]
    except KeyError:
        print(f"Error: Starting location not found in the adjacency list.")
        return[]
    
    visited = []
    queue = [start]
    
    while queue:
        current = queue.pop(0)
        
        if current not in visited:
            visited.append(current)
            neighbors = adj_list.get(current)
            if neighbors is None:
                neighbors = []
            for neighbor in neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    return visited


if __name__ == '__main__':
    visited_locations = bfs(ROUTES, 'Rutland')
    print("Visited Locations:", visited_locations)    