class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        # key存在在字典中
        # 从字典中找到节点
        node = self.cache[key]

        # 调整位置
        # 1.删除node
        node.next.prev = node.prev
        node.prev.next = node.next
        # 2.添加至head后面
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

        return node.val

    def put(self, key, val):
        if key in self.cache:
            # 如果key已经存在
            node = self.cache[key]
            # 调整位置
            # 1.删除node
            node.next.prev = node.prev
            node.prev.next = node.next
            # 2.添加至head后面
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
            node.val = val

        else:
            # key 不存在
            # 超过容量
            if len(self.cache) >= self.capacity:
                # 删除字典
                index = self.tail.prev.key
                del self.cache[index]
                # 删除tail前一个节点
                del_node = self.tail.prev
                del_node.prev.next = self.tail
                self.tail.prev = del_node.prev
            node = Node(key, val)
            # 加入字典
            self.cache[key] = node
            # 加入链表
            node.next = self.head.next
            node.prev = self.head
            self.head.next = node
            node.next.prev = node
