class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root: TreeNode):
    result = []
    queue = [root]

    while queue:
        sum = 0
        count = 0
        temp = []
        while queue:
            node = queue.pop(0)
            sum += node.val
            count += 1
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
        queue = temp
        result.append(sum / count)

    return result
