from pprint import pprint as pp
from heapq import heappush, heappop
from collections import defaultdict

have_times = False
subway = defaultdict(lambda:{})
routes = {}

def shortest_routes(origin):
    """
    Returns dictionary of shortest routes from the origin station
    to every other reachable station. Uses a priority queue 
    implementation of Dijkstra's algorithm.

    Arguments:
    origin -- name of the origin subway station
    """
    paths = {}
    queue = [(
        0,       # path distance
        origin,  # current station
        [origin] # path up to current station
    )]
    while queue:
        path_dist, vertex, path = heappop(queue)
        if vertex not in paths: # unvisited
            paths[vertex] = (path_dist, path)
        for next_vertex, edge_dist in subway[vertex].items():
            if next_vertex not in paths:
                total_dist = path_dist + edge_dist
                heappush(queue, (
                    path_dist + edge_dist,
                    next_vertex,
                    path + [next_vertex]
                ))
    return paths

def add_train_line(stops, name, time_between_stations=None):
    """
    Adds a train line to the subway. 

    Arguments:
    stops -- a unique list of subway stops
    name -- the name of the subway line

    Keyword arguments:
    time_between_stations -- a list of tuples corresponding to stops
        defining the time between stops, e.g. [('Houston','14th',12) .. ]
    """
    # invalidate all calculated, in-memory shortest routes
    routes = {}
    # remember whether or not edge lengths were provided
    global have_times
    if not have_times:
        have_times = bool(time_between_stations)
    # construct time_between_stations if not provided (with time=1)
    time_between_stations = time_between_stations or zip(
        stops[0:len(stops)-1],
        stops[1:len(stops)],
        [1]*len(stops),
    )
    # add station-to-station connections to subway graph
    for stop1, stop2, dist in time_between_stations:
        # add bi-directional edges
        subway[stop1][stop2] = dist
        subway[stop2][stop1] = dist

def take_train(origin, destination):
    """
    Returns shortest path and estimated travel time.
    
    Arguments:
    origin -- name of origin subway station
    destination -- name of destination subway station

    Returns:
    if travel times have been provided:
        (path,time)
    else, don't include time:
        path
    """
    # calculate and save all shortest routes for origin if not already in memory
    if origin not in routes or destination not in routes[origin]:
        routes[origin] = shortest_routes(origin)
    # format return value based on whether or not route times were provided
    time, path = routes[origin][destination]
    if have_times:
        return (path,time)
    return path

if __name__ == "__main__":
    add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1",
        time_between_stations=[
            ("Canal", "Houston", 3),
            ("Houston", "Christopher", 7),
            ("Christopher", "14th", 2),
    ])
    add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E",
        time_between_stations=[
            ("Spring", "West 4th", 1),
            ("West 4th", "14th", 5),
            ("14th", "23rd", 2),
    ])
    print take_train(origin="Houston", destination="23rd")
