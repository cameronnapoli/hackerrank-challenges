# is valid BST

class Btree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

t1 = Btree(5, Btree(3,Btree(2),Btree(4)), Btree(7,Btree(6),Btree(8))) # valid
t2 = Btree(5, Btree(6), Btree(4)) # invalid

# checks if the binary tree, is a valid binary search tree
def isValidBST(btree):
    # If empty node hit return true
    if btree == None:
        return True
    if btree.left != None and not (btree.left.value < btree.value) or \
            btree.right != None and not (btree.right.value > btree.value):
        return False
    return isValidBST(btree.left) and isValidBST(btree.right)


print( isValidBST(t1) )
print( isValidBST(t2) )
