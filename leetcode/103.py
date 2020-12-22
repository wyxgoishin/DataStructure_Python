"""
题目描述：
    给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
题解：
    因为题目只对输出做要求，因此采用普通的层次遍历加上对各层遍历结果进行变换即可
    层次遍历采用数组隔离法实现即可
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    res, cur, sign = [], [root], False
    while cur:
        cur_res, nxt_cur = [], []
        for node in cur:
            if(node):
                cur_res.append(node.val)
                nxt_cur.extend([node.left, node.right])
        if cur_res:
            if sign:
                cur_res = cur_res[::-1]
            res.append(cur_res)
        cur = nxt_cur
        sign = False if sign else True
    return res

tree = TreeNode(10)
tree.left, tree.right = TreeNode(3), TreeNode(93)
tree.left.right, tree.right.left = TreeNode(12), TreeNode(83)
print('zigzagLevelOrder:', end='')
print(zigzagLevelOrder(tree))