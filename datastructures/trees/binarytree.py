from datastructures.trees.node import Node


class BinaryTree:
    """
    A binary tree class containing integer values.
    """
    def __init__(self):
        self.root = None

    # Inserts a new value into the binary tree.
    def insert(self, value):

        # Is root empty?
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            parent = None
            left_child = False

            # Loop until we find an available space.
            while current is not None:
                parent = current

                if value < current.value:
                    current = current.left
                    left_child = True

                elif value == current.value:
                    current.number += 1
                    return

                else:
                    current = current.right
                    left_child = False

            # Insert new node in left or right child.
            if left_child:
                parent.left = Node(value)
            else:
                parent.right = Node(value)

    # Removes a value from the binary tree.
    def remove(self, value):
        self.root = self._remove(self.root, value)

    # Internal recursive method for removal.
    def _remove(self, node, value):
        # Base case.
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            # Node with one or no child.
            if node.left is None:
                tmp = node.right
                return tmp
            elif node.right is None:
                tmp = node.left
                return tmp
            else:
                # Node with two children
                # Get the in-order successor (smallest in the right subtree)
                current = node.right
                while current.left is not None:
                    current = current.left

                # Copy the in-order successor's value to this node
                node.value = current.value

                # Delete the in-order successor
                node.right = self._remove(node.right, current.value)

    # Prints out all the values in the binary tree.
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            raise Exception("Root is empty, cannot print tree.")

    # Internal recursive method for printing values.
    def _print_tree(self, node):
        if node is not None:
            # In-order traversal of the tree.
            self._print_tree(node.left)
            print(str(node.value), end=" ")
            self._print_tree(node.right)

    # Checks if tree is empty.
    def is_empty(self):
        return self.root is None
