class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val
        
class Deque:
    
    def __init__(self):
        self.head = Node(-1) # dummy node
        self.tail = self.head

    def isEmpty(self) -> bool:
        if self.head.next:
            return False
        else:
            return True

    def append(self, value: int) -> None:
        new_node = Node(value)

        if self.isEmpty():
            self.head.next = new_node
            self.tail = new_node
            new_node.prev = self.head
        else:
            tmp = self.tail
            self.tail = new_node
            tmp.next = new_node
            new_node.prev = tmp


 

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.tail = new_node
            self.head.next = new_node
            new_node.prev = self.head
        else:
            tmp = self.head.next
            self.head.next = new_node
            new_node.next = tmp
            tmp.prev = self.head.next
            new_node.prev = self.head
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1     

        tmp = self.tail
        self.tail = tmp.prev
        self.tail.next = None
        return tmp.val


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.head.next
        
        if not self.head.next.next:
            self.head.next = None
            self.tail = None
        else:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        
        return tmp.val
