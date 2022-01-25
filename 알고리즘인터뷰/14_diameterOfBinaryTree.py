class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def creatBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = creatBTree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = creatBTree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode


lst = [1,2,3,4,5,6]
root = creatBTree(lst, 0)
class Solution:
    longest: int =0

    def diameterOfBinaryTree(self, root:TreeNode)-> int:
        def dfs(node: TreeNode)->int:

            if node is None:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2)
            print(f'node.val: {node.val}')
            print(max(left, right) + 1)
            return max(left, right) + 1

        dfs(root)
        return self.longest

a = Solution()
print(a.diameterOfBinaryTree(root))