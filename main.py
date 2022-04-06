"""Simple binary tree module"""
# import functools
# import operator

class Node:
    """Class represents a binary tree node"""
    def __init__(self, L, R, n) -> None:
        self.left = L
        self.right = R
        self.value = n

    def insert(self, value):
        """Method for inserting a node"""
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(None, None, value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(None, None, value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def print_tree(self):
        """Print tree from min to max"""
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()

    def __str__(self):
        return f"Node(value={self.value})"

root = Node(None, None, 3)

for i in range(1, 6, 1):
    root.insert(i)

def flatten(s):
    """Recuisevelly flater a list"""
    if s == []:
        return s
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])

def get_layer(node):
    """Get layer"""
    values = []

    if node.left is not None:
        values.append(node.left.value)
    if node.right is not None:
        values.append(node.right.value)

    if node.left is not None:
        values.append(get_layer(node.left))
    if node.right is not None:
        values.append(get_layer(node.right))
    return values


def tree_by_levels(node):
    """Returs list of tree values by levels"""
    values = [[node.value]]
    values.append(get_layer(node))
    return flatten(values)

print(tree_by_levels(root))
