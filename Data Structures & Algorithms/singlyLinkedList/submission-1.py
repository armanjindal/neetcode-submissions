class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1) # Dummy head node
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next # iterates
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node
        # Edge case - empty list 
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next         


    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while curr:
            if i == index and curr.next:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            curr = curr.next
            i += 1
        return False

                

    def getValues(self) -> List[int]:
        curr = self.head.next
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals
