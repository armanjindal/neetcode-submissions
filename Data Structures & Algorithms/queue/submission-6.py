class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val
        
class Deque:
    
    def __init__(self):
        self.head = Node(-1) # dummy node
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        
        tmp = self.tail.prev
        tmp.next = new_node
        new_node.prev = tmp
        new_node.next = self.tail 
        self.tail.prev = new_node


    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        tmp = self.head.next
        tmp.prev = new_node

        new_node.prev = self.head
        new_node.next = tmp 

        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        old_tail = self.tail.prev
        new_tail = old_tail.prev

        self.tail.prev = new_tail
        new_tail.next = self.tail 

        return old_tail.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        old_head = self.head.next
        new_head = old_head.next

        self.head.next = new_head
        new_head.prev = self.head
        return old_head.val
