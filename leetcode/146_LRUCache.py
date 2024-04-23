from collections import defaultdict 
"""
Hashmap + Doubly LinkedList
Doubly Linked List is effective in deleting node on any position
Use hashmap to store nodes of doubly linked list

Edge case: same key
"""
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionary = defaultdict(ListNode)
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if not key in self.dictionary.keys():
            return -1
        
        node = self.dictionary[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.dictionary.keys():
            node = self.dictionary[key]
            self.remove(node)
            self.dictionary[key].val = value
            self.add(node)
        
        if not key in self.dictionary.keys():
            node = ListNode(key, value)
            self.add(node)
            self.dictionary[key] = node
            if len(self.dictionary.keys()) > self.capacity:
                del self.dictionary[self.tail.prev.key]
                self.remove(self.tail.prev)

    def add(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


        

