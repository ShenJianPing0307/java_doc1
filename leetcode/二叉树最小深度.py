"""
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2
              3
            /    |
           9     20
               /   |
              15   7
解题思路：遍历每一层的节点，遍历到叶子节点没有子节点的节点即可，每一层就是一个高度。
        我们可以这样思考通过层序遍历的方式，使用队列来存取所有的元素
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = [root]
        depth = 0

        while queue:
            depth += 1

            for i in range(len(queue)):
                node = queue.pop(0)  # 先进先出

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return depth
