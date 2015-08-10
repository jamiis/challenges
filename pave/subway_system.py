from pprint import pprint as pp
from heapq import heappush, heappop
from collections import defaultdict

have_times = False
subway = defaultdict(lambda:{})

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

def add_train_line(stops, name, time_between_stations=None):
    # remember whether or not edge lengths were provided
    have_times = bool(time_between_stations)
    # constructs time_between_stations (with time=1) if not provided
    time_between_stations = time_between_stations or zip(
        stops[0:len(stops)-1],
        stops[1:len(stops)],
        [1]*len(stops),
    )
    # adds station-to-station connections to subway graph
    for stop1, stop2, dist in time_between_stations:
        # adds bi-directional edges
        subway[stop1][stop2] = dist
        subway[stop2][stop1] = dist

def take_train(origin, destination):
    # calculate shortest paths
    # optional: memoize shortest paths?
    # return shortest path and, conditionally, distance
    pass

if __name__ == "__main__":
    add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1",
        time_between_stations=[("Canal", "Houston", 3),
                               ("Houston", "Christopher", 7),
                               ("Christopher", "14th", 2),
                               ])
    add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E",
        time_between_stations=[("Spring", "West 4th", 1),
                               ("West 4th", "14th", 5),
                               ("14th", "23rd", 2),
                               ])
    pp(shortest_paths(subway, 'Houston'))
