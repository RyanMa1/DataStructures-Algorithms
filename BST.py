class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root == None:
            self.root = Node(new_val)
        node = self.root
        prev = None
        while node != None:
            if new_val < node.value:
                prev = node
                node = node.left
            elif new_val > node.value:
                prev = node
                node = node.right
        
        if new_val < prev.value:
            prev.left = Node(new_val)
        else:
            prev.right = Node(new_val)
        pass

    def search(self, find_val):
        node = self.root
        while node != None:
            if find_val < node.value:
                node = node.left
            elif find_val > node.value:
                node = node.right
            else:
                return True
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(10)
tree.insert(-3)
# Check search
# Should be True
print (tree.search(-3))
# Should be False
print (tree.search(6))