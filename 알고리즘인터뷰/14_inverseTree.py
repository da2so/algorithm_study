import collections


class TreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

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
    print(root.data, end=' ')

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

            print(x.data, end=' ')

            # enqueue left and right child of `x` to the first queue
            if x.left:
                q1.append(x.left)

            if x.right:
                q1.append(x.right)

            # dequeue front node from the second queue and print it
            y = q2.popleft()

            print(y.data, end=' ')

            # enqueue right and left child of `y` to the second queue
            if y.right:
                q2.append(y.right)

            if y.left:
                q2.append(y.left)

lst = [4,2,7,1,3,6,9]
root = creatBTree(lst, 0)

def inverseTree(root: TreeNode) -> TreeNode:

    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

printNodes(root+'\n')
root = inverseTree(root)
printNodes(root)



