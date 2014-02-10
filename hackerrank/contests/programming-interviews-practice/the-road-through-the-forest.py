from sys import argv
from pprint import pprint

class Forest():
    def __init__(self, trees):
        self.trees = trees
        self.height = len(self.trees)
        self.width  = len(self.trees[1])

    def is_valid_tree(self, pos):
        r, c = pos
        return r >= 0 and r < self.height and c >= 0 and c < self.width

    def min_trees_cut(self):
        ''' calculate the minimum number of trees you need to cut 
        to get to the other side of the forest. 
        uses specialized dfs with pruning. '''

        def possible_moves(pos):
            ''' returns a list of possible moves from a position. '''
            r, c = pos
            # below pictorially represents possible moves
            possible = [
                (r-1,c-1),          (r-1,c+1), 
                (r,  c-1),          (r,  c+1), 
                (r+1,c-1), (r+1,c), (r+1,c+1),
            ]
            # filter out invalid moves
            return filter(self.is_valid_tree, possible)

        # min cuts will *always* be <= forest height
        min_cuts = self.height 
        # iterate over starting points
        for start_col in xrange(self.width):
            path = []
            cuts = 0
            stack = [(0, start_col)]
            while stack:
                pos = stack.pop()
                # if pos: cuts += 1
                if pos not in path:
                    path.append(pos)
                    pprint(path)
                for move in possible_moves(pos):
                    if move not in path:
                        stack.append(move)
        return self.height

def parse_forests():
    f = open(argv[1], 'r')
    num_forests = int(f.readline())
    while num_forests:
        height, _ = map(int, f.readline().split())
        # fill 2d list of trees
        trees = []
        for _ in xrange(height):
            trees.append(map(int, f.readline().split()))
        # decrement counter
        num_forests = num_forests - 1
        yield Forest(trees)

if __name__ == '__main__':
    for forest in parse_forests():
        pprint(forest.min_trees_cut())
