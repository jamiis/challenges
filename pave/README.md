This is a simple module for adding trains to a subway
and finding the shortest path between stations.
The shortest path is found using Dijkstra's algorithm 
which I implemented using a priority queue. In the situation
that station-to-station times were not provided, `take_train`
does not return an estimated time, only the shortest path.

A few implementation thoughts:
- If the plan was to increase increase the size of this module, it would be wise to begin abstracting pieces into Classes, e.g. the subway object should be a `Graph` class.
- There is no guarantee this follows PEP 8 and I would follow a custom pylint style file if I were programming in a professional environment.
- In hindsight I would have built out a `Graph` class first vs. refactoring code. A `Graph` class would make the code more mentally parsable and allow it to grow more easily.
- Testing is done by running `python subway_system`. I only test the examples given in the email. With more time I would add more extensive unit testing to each function ontop of also adding more integration testing. I would also probably use a testing framework like `pytest`.
