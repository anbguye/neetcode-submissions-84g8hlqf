class Node:

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):

        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:

        if index >= self.size or index < 0:
            return -1
        
        curr = self.head.next

        for i in range(index):
            curr = curr.next

        return curr.val 

    def addAtHead(self, val: int) -> None:
        
        curr = Node(val, self.head.next, self.head)
        self.head.next.prev = curr
        self.head.next = curr
        self.size += 1

    def addAtTail(self, val: int) -> None:
        
        curr = Node(val, self.tail, self.tail.prev)
        self.tail.prev.next = curr
        self.tail.prev = curr
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size or index < 0:
            return

        curr = self.head

        for i in range(index):
            curr = curr.next

        new_node = Node(val, curr.next, curr)
        curr.next.prev = new_node
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size or index < 0:
            return    

        curr = self.head.next

        for i in range(index):
            curr = curr.next
            
        curr.prev.next, curr.next.prev = curr.next, curr.prev
        self.size -=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)