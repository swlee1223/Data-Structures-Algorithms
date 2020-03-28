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
        right = heapq.heappop(heap)

        heapq.heappush(heap, InnerNode(left, right))
    
    return(heapq.heappop(heap))


def build_codes(tree: Node) -> Dict[str, str]:
    """
    :param node: a Huffman tree
    :return: codes for all characters in the Huffman tree
    """
    def traverse(tree, code, code_map):
        # base case for recursion
        if isinstance(tree, Leaf):
            code_map[tree.character]= code
            
        else:
            assert isinstance(tree, InnerNode)
            traverse(tree.left, code + '1', code_map)
            traverse(tree.right, code + '0', code_map)


    code_map = {}
    traverse(tree, '', code_map)

    return(code_map)
    
# given code map, decodes based on the frequency of the words.
def encode(code_map):
    return(''.join(code_map[l] for l in text))

# use the tree to decode the encoded text.
def decode(encoded_text, tree):
    decoded_text = ''
    node = tree
    i = 0
    while i < len(encoded_text):
        assert encoded_text[i] in ["0", "1"]
        while isinstance(node, InnerNode):
            if encoded_text[i] == "0":
                node = node.right
            else:
                node = node.left

            i += 1

        assert isinstance(node, Leaf)
        decoded_text += node.character
        node = tree

    return(decoded_text)

def print_statement(res, fname):
    print(fname + ' : ' + str(res))

if __name__ =='__main__':
    text = "AAAAAAAAAABBBBBBBBBCCCCCCDDDEF"
    frequencies = compute_frequences(text)
    print_statement(frequencies, 'Computing Frequences')
    tree = build_tree(frequencies)
    print_statement(tree, 'Build Tree')
    code_map = build_codes(tree)
    print_statement(code_map, 'Build Codes')
    encoded_text = encode(code_map)
    print_statement(encoded_text, 'Encode')
    decoded_text = decode(encoded_text, tree)
    print_statement(decoded_text, 'Decode')
    print_statement(text == decoded_text, "Decoded text same as original text? \n ===> Response")