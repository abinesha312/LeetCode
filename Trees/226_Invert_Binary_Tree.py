from typing import Optional


class TreeNode:
    def __init__(self,val=0, left=None, right= None):
        self.val = None
        self.left = left
        self.right = right

class solution:
    def InvBinTree(self,root: TreeNode)->TreeNode:
        if not root:
            return None
        root.left, root.right = root.right,root.left

        self.InvBinTree(root.left)
        self.InvBinTree(root.right)
        return root
    


if __name__ == "__main__":
    inputt = [1,2,3,4,5,6,7,8,9]
    cc = solution().InvBinTree(inputt)
    print(cc)