class Node(object):          # 定义一个树的节点对象
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):          # 定义树类
    def __init__(self):
        self.root = None

    def add(self, item):     # 添加节点的方法
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)     # 移除并返回queue队列首元素
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):          # 广度遍历的方法
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, root):             # 先序遍历的方法（根左右）
        if root is None:
            return
        print(root.elem, end=" ")         # 不换行，仅添加“ ”空格
        self.preorder(root.lchild)
        self.preorder(root.rchild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")                    # 换行
    tree.preorder(tree.root)

# 根据中序和先序（或中序和后序）可以来确定一颗二叉树





