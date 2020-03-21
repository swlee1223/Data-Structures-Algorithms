from abc import ABC, abstractmethod
from typing import Dict


class Node(ABC):
    @abstractmethod
    def get_frequency(self):
        pass

    def __lt__(self, other):
        return self.get_frequency() < other.get_frequency()


class InnerNode(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right
        self.frequency = left.get_frequency() + right.get_frequency()

    def get_frequency(self):
        return self.frequency

    def __repr__(self):
        return "IN({} {})".format(self.left, self.right)


class Leaf(Node):
    def __init__(self, character: str, frequency: int):
        self.character = character
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def __repr__(self):
        return self.character


def compute_frequences(text: str) -> Dict[str, int]:
    frequences = {}
    for x in text:
        frequences[x] = frequences.get(x, 0) + 1
    
    return(frequences)


# Using implementation of heapify and classes (including abstract class) defined above
def build_tree(frequencies: Dict[str, int]) -> Node:
    '''
    :param frequencies: dictionary with keys as the letters and values as frequencies
    :return Node : returns a tree
    '''

    import heapq
    heap = [Leaf(k, v) for (k, v) in frequencies.items()]

    # Priority Queue (non-decreasing)
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        # print('Left letters is ' + str(left))
        # print('Left frequencies are ' + str(left.frequency))
        right = heapq.heappop(heap)
        # print('Right letters is ' + str(right))
        # print('Right frequencies are ' + str(right.frequency))
        

        heapq.heappush(heap, InnerNode(left, right))
        # print('Current heap is ' + str(heap))
    
    return(heapq.heappop(heap))


def build_codes(tree: Node) -> Dict[str, str]:
    """
    :param node: a Huffman tree
    :return: codes for all characters in the Huffman tree
    """
    def traverse(tree, code, code_map):
        # base case for recursion
        if isinstance(tree, Leaf):
            # print("Passed Leaf Part")
            code_map[tree.character]= code
            
        else:
            # print("Passed InnerNode Part")
            assert isinstance(tree, InnerNode)
            traverse(tree.left, code + '1', code_map)
            # print("Does this pass here?")
            traverse(tree.right, code + '0', code_map)


    code_map = {}
    traverse(tree, '', code_map)

    return(code_map)
    

def encode(text):
    frequencies = compute_frequences(text)
    tree = build_tree(frequencies)
    code_map = build_codes(tree)

    return(''.join(code_map[l] for l in text))


# going to implement soon,=
def decode(encoded_text):
    pass

text = "AAAAAAAAAABBBBBBBBBCCCCCCDDDEF"
encoded_text = encode(text)
print(encoded_text)
