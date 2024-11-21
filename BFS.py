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

queue = []

bfs(adjency_list, key):
    while adjency_list:
        for x in adjency_list.values(key):
            queue.append(x)
        

if __name__ == '__main__':
    key = input('Where would you like to start?')
    