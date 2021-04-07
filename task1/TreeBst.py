import pickle

class Node:
    '''Node which holds val and noun_list'''
    def __init__(self, val, noun_list):
        self.val = val
        self.noun_list = noun_list
    def __str__(self):
        return f"<{self.val}::{self.noun_list}>\n"

class TreeBst:
    def __init__(self, data):
        '''The tree structure'''
        self.leftChild = None
        self.rightChild = None
        self.data = data

    def insert(self, data):
        '''For inserting the nodes'''
        if self.data.val == data.val:
            return False
        elif self.data.val > data.val:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = TreeBst(data)
                return True
        elif self.data.val < data.val:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = TreeBst(data)
                return True

    def preorder(self):
        '''For preorder traversal of the TreeBst '''
        if self:
            print(str(self.data), end = '')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()


# if __name__ == '__main__':
#     tree = TreeBst(Node(5, ['Harry', 'Sagnik']))
#     tree.insert(Node(12, ["English"]))
#     tree.insert(Node(2, ['Ron', 'Hermione']))
#
#     #add many number of nodes and check if it works.
#
#     with open("tree.pkl", 'wb') as f:
#         pickle.dump(tree, f)
#     #a new file tree.pkl should be created at this point
#     with open('tree.pkl', 'rb') as f:
#         treeNew = pickle.load(f)
#
#     treeNew.insert(Node(3, ['After pickle']))
#     treeNew.preorder()
