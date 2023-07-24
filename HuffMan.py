from typing import Dict, Tuple

def huffman_code(string: str) -> Dict[str, str]:
    """
    Generates the Huffman code for a given string.

    Args:
    - string (str): The input string.

    Returns:
    - A dictionary mapping each character to its Huffman code.
    """
    class NodeTree:
        """
        Tree node class for Huffman coding.
        """
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

        def children(self) -> Tuple:
            """
            Returns the children of the node as a tuple.
            """
            return (self.left, self.right)

        def nodes(self) -> Tuple:
            """
            Returns the nodes of the tree as a tuple.
            """
            return (self.left, self.right)

        def __str__(self) -> str:
            """
            Returns the string representation of the node.
            """
            return f'{self.left}_{self.right}'

    def huffman_code_tree(node: NodeTree, left: bool = True, bin_string: str = '') -> Dict[str, str]:
        """
        Recursively generates the Huffman code for a given node in the Huffman tree.

        Args:
        - node (NodeTree): The node in the Huffman tree.
        - left (bool): A flag indicating whether the current node is a left child.
        - bin_string (str): The binary string representing the Huffman code.

        Returns:
        - A dictionary mapping each character to its Huffman code.
        """
        if isinstance(node.left, str):
            return {node.left: bin_string}
        left_child = huffman_code_tree(node.left, True, bin_string + '0')
        right_child = huffman_code_tree(node.right, False, bin_string + '1')
        code_dict = {}
        code_dict.update(left_child)
        code_dict.update(right_child)
        return code_dict

    # Calculate the frequency of each character in the string.
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1

    # Sort the frequency dictionary by the frequency of each character.
    freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Create a list of nodes from the frequency dictionary.
    nodes = [(NodeTree(char), count) for char, count in freq_sorted]

    # Build the Huffman tree.
    while len(nodes) > 1:
        key1, count1 = nodes.pop()
        key2, count2 = nodes.pop()
        node = NodeTree(key1, key2)
        nodes.append((node, count1 + count2))
        nodes.sort(key=lambda x: x[1], reverse=True)

    # Generate the Huffman code for each character.
    huffman_code_dict = huffman_code_tree(nodes[0][0])

    return huffman_code_dict


if __name__ == '__main__':
    string = input('Type Your Text: ')
    huffman_code_dict = huffman_code(string)

    print(' Char | Huffman code ')
    print('----------------------')
    for char, code in sorted(huffman_code_dict.items()):
        print(f' {char:<4} |{code:>12}')

    input('Press Enter to exit')