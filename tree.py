class Node:
    def __init__(self, data):
        """Constructor to initialise a node
        """
        # store data
        self.data = data
        # store reference of the items on the left and right
        self.left = None
        self.right = None


class Tree:
    def insert(self, root, data):
        """Add a node following the binary tree rules. If the value of the node is smaller than the root, it is placed on the left and conversely.
        """
        if root == None:
            root = Node(data)

        else:
            if data < root.data:
                following = self.insert(root.left, data)
                root.left = following

            else:
                following = self.insert(root.right, data)
                root.right = following

        return root


    def searchheight(self, root, count):
        """Recursive function to search the height maximum.
        """
        if root == None:
            return count

        return max(self.searchheight(root.left, count + 1), self.searchheight(root.right, count + 1))


    def getheight(self, root):
        """Return the height of the tree, the number of edges between the tree's root and its furthest leaf
        """
        return self.searchheight(root, -1)


    def levelOrder(self, root):
        """Return the level-order traversal of the binary search tree, which the tree's nodes are sorted from left to right, top to bottom.
        """
        transversal = []
        tree = [root]

        while len(tree) != 0:
            transversal.append(tree[0].data)
            if tree[0].left != None:
                tree.append(tree[0].left)
            if tree[0].right != None:
                tree.append(tree[0].right)
            tree.pop(0)

        return transversal




if __name__ == "__main__":

    with open('example.txt') as f:
        lines = [int(line) for line in f]

    num_elements = lines[0]
    tree_elements = lines[1:]
    root = None
    my_tree = Tree()
    for element in tree_elements:
        root = my_tree.insert(root, element)


    print(my_tree.levelOrder(root))
    root = my_tree.removeDuplicates(root)
    print(my_tree.levelOrder(root))



