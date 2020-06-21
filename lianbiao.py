# #链表：基本的数据结构，一种线性表，每个元素附带一个节点，该节点指向下一个元素的地址。最后元素节点为None
# 单链表：只能由前一个元素的节点访问下一个元素，不能反向
# 单链表示例：


# class Node(object):
#     def __init__(self, elem):
#         self.elem = elem          # 元素Node中的元素
#         self.next = None          # 元素Node中的节点


# #单链表初始状态下包含一个空head，指向第一个元素Node地址


class SingleLinkList(object):     # 单链表的一些操作方法
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):            # 判断链表是否为空
        return self._head == None  # 头元素为空

    def length(self):             # 返回链表长度
        cur = self._head    # 定义cur游标，指向头元素
        count = 1           # count计数为1
        while cur != None:  # 如果元素不为空
            count += 1
            cur = cur.next
        return count

    def travel(self):             # 遍历整个链表
        cur = self._head          # 定义cur游标，指向头元素
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):          # 链表首部添加元素
        node = Node(item)         # 定义要添加的元素node实例
        node.next = self._head    # 将head指向的首元素地址赋给node
        self._head = node         # 将元素node给head

    def append(self, item):       # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):       # 链表指定位置pos添加元素item
        pre = self._head
        count = 0
        while count < (pos-1):
            count +=1
            pre = pre.next
        node = Node(item)
        node.next = pre.next
        pre.next = node

    def remove(self):             # 移除链表元素
        pass

    def search(self, item):       # 查询链表元素是否存在
        pass


# if __name__ == "__main__":
#     ll = SingleLinkList()
#     print(ll.is_empty())        # True
#     print(ll.length())          # 1
#     ll.append(1)                # ll = 1
#     print(ll.is_empty())        # False
#     print(ll.length())          # 2
#     ll.append(2)                # ll = 1,2
#     ll.append(4)                # ll = 1,2,4
#     ll.insert(2, 9)             # ll = 1,2,9,4(在2号位：第三个元素插入9，即第三个元素为9)
#     ll.append(6)                # ll = 1,2,9,4,6
#     ll.travel()


# 单向循环链表：链表尾部的next不为None，而是指向首元素
# 双向链表：每个元素附带两个节点，prev和next，指向前后元素。
# 第一个元素的prev节点和最后元素的next节点为None。

class Node(object):
    def __init__(self, item):
        self.elem = item          # 元素Node中的元素
        self.next = None          # 元素Node中的节点
        self.prev = None          # 元素Node中的节点


class DoubleLinkList(object):     # 双链表的一些操作方法
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):            # 判断链表是否为空
        return self._head == None  # 头元素为空

    def length(self):             # 返回链表长度
        cur = self._head    # 定义cur游标，指向头元素
        count = 1           # count计数为1
        while cur != None:  # 如果元素不为空
            count += 1
            cur = cur.next
        return count

    def travel(self):             # 遍历整个链表
        cur = self._head          # 定义cur游标，指向头元素
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):          # 链表首部添加元素
        node = Node(item)         # 定义要添加的元素node实例
        node.next = self._head    # 将head指向的首元素地址赋给node
        self._head = node         # 将元素node给head
        node.next.prev = node

    def append(self, item):       # 链表尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):       # 链表指定位置pos添加元素item
        pre = self._head
        count = 0
        while count < (pos-1):
            count += 1
            pre = pre.next
        node = Node(item)
        node.next = pre.next
        node.prev = pre
        pre.next = node
        pre.next.prev = node.next

    def remove(self):             # 移除链表元素
        pass

    def search(self, item):       # 查询链表元素是否存在
        pass


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())        # True
    print(ll.length())          # 1
    ll.append(1)                # ll = 1
    print(ll.is_empty())        # False
    print(ll.length())          # 2
    ll.append(2)                # ll = 1,2
    ll.append(4)                # ll = 1,2,4
    ll.insert(2, 9)             # ll = 1,2,9,4(在2号位：第三个元素插入9，即第三个元素为9)
    ll.append(6)                # ll = 1,2,9,4,6
    ll.travel()

