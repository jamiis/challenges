from pprint import pprint as pp
from heapq import heappush, heappop

def shortest_paths(graph, start):
    """
    Returns dictionary of shortest paths from the start node
    to every other reachable node. Uses priority queue implementation 
    of Dijkstra's algorithm.
    """
    shortest_paths = {}
    queue = [(
        0,          # path distance
        start,      # current vertex
        [start]     # path to current vertex
    )]
    while queue:
        path_dist, vertex, path = heappop(queue)
        if vertex not in shortest_paths: # unvisited
            shortest_paths[vertex] = (path_dist, path)
        for next_vertex, edge_dist in graph[vertex].items():
            if next_vertex not in shortest_paths:
                total_dist = path_dist + edge_dist
                heappush(queue, (
                    path_dist + edge_dist,
                    next_vertex,
                    path + [next_vertex])
                )
    return shortest_paths

def add_train_line(stops, name):
    pass

def take_train(origin, destination, time_between_stations=None):
    pass

if __name__ == "__main__":
    graph = {
        'a': { 'a':0, 'b':5, 'c':7, 'd':9, 'e':25 },
        'b': { 'a':5, 'b':0, 'c':3, 'd':8 },
        'c': { 'a':7, 'b':3, 'c':0, 'd':1 },
        'd': { 'a':9, 'b':8, 'c':1, 'd':0 },
        'e': { 'a':25 },
    }
    pp(shortest_paths(graph, 'b'))
