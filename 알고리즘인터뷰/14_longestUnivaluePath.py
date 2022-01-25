#동일한 값을 지닌 가장 긴 경로를 찾아라

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


lst = [5,4,5,1,1,5]
root = creatBTree(lst, 0)

class Solution:
    longest: int = 0

    def longestpath(self, root:TreeNode)->int:

        def dfs(node:TreeNode):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left  and node.left.val == node.val:
                left +=1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left+right)

            return max(left, right)
        dfs(root)
        return self.longest

a = Solution()
print(a.longestpath(root))