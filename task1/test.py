import pickle
with open('tree.pkl', 'rb') as f:
    treeNew = pickle.load(f)

treeNew.preorder()

# from TreeBst import TreeBst, Node
#
# tree = TreeBst(Node(0, ['main']))
# tree.insert(Node(1, ['hello']))
#
# tree.preorder()
