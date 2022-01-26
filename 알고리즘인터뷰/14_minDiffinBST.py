
# 두노드간의 갑차이가 가장 작은값을 출력
import collections
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


def printNodes(root):
    # return if the tree is empty
    if root is None:
        return

    # print the root node
    print(root.val, end=' ')

    # create two empty queues and enqueue root's left and
    # right child, respectively
    q1 = collections.deque()
    q2 = collections.deque()

    if root.left and root.right:
        q1.append(root.left)
        q2.append(root.right)

    # loop till queue is empty
    while q1:

        # calculate the total number of nodes at the current level
        n = len(q1)

        # process every node of the current level
        for _ in range(n):

            # dequeue front node from the first queue and print it
            x = q1.popleft()

            print(x.val, end=' ')

            # enqueue left and right child of `x` to the first queue
            if x.left:
                q1.append(x.left)

            if x.right:
                q1.append(x.right)

            # dequeue front node from the second queue and print it
            y = q2.popleft()

            print(y.val, end=' ')

            # enqueue right and left child of `y` to the second queue
            if y.right:
                q2.append(y.right)

            if y.left:
                q2.append(y.left)


class Solution:
    result: int = 100000
    prev: int = 1000000
    def minDiffinBST(self, root:TreeNode)->int:

        if root.right:
            self.minDiffinBST(root.right)

        self.result = min(self.result, self.prev - root.val)
        self.prev = root.val

        if root.left:
            self.minDiffinBST(root.left)

        return self.result



root = [4,2,6,1,3,None,None]
root = [10,4,15,1,8,None,None]

root = creatBTree(root, 0)

a = Solution()
print(a.minDiffinBST(root))