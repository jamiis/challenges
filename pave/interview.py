from collections import defaultdict
dictionary = [
    'aardvark',
    'zebra',
]

t9 = {
    'a':'1',
    'b':'1',
    'c':'1',
}

class Node(object):
    # children = { '0': None }
    _children = defaultdict(lambda:None)
    _words = []

    def __init__(self):
        pass

    def has_child(self, number):
        return bool(node._children[number]):

    def new_child(self, number):
        # TODO node already exists?
        self._children[number] = Node()

    def add_word(self, word):
        self._words.append(word)

    def get_child(self, number):
        return self._children(number)

class Tree(object):
    root = Node()

    def __init__(self):
        pass

    def insert(word):
        node = root
        for index, letter in enumerate(word):
            number = t9[letter]
            # adds branch if branch doesnt exist
            if not node.has_child(number):
                node.new_child(number)
            # traverse one-step down branch
            node = get_child(number)
            # adds word to leaf
            if index == len(word)-1:
                node.add_word(word)

    def search(self, number):
        words = []
        node = self.root
        # traverse to node
        for n in number:
            # TODO handle failure if node doesn't exist
            node = node.get_child(n)
        # append node.words to words
        for nod in node.bfs():
            words.append(nod.get_words())
        # return flattened words list
        return chain.flatten(words)

def build_t9(dictionary):
    tree = Tree()
    for word in dictionary:
        tree.insert(word)
    return tree

if __name__ == "__main__":
    print build_t9(dictionary)

