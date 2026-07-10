class Node:

    def __init__(self, val="", prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):

        self.head = Node("", None, None)
        self.tail = Node("", None, None)
        home = Node(homepage, self.head, self.tail)
        self.curr = home
        self.head.next = home
        self.tail.prev = home

    def visit(self, url: str) -> None:
        
        self.curr.next = Node(url, self.curr, self.tail)
        self.tail.prev = self.curr.next
        self.curr = self.curr.next
        print(self.curr.val)


    def back(self, steps: int) -> str:
        
        while steps > 0 and self.curr.prev and self.curr.prev.val != "":

            steps -= 1
            self.curr = self.curr.prev

            print(self.curr.val)
        return self.curr.val

    def forward(self, steps: int) -> str:
        
        while steps > 0 and self.curr.next and self.curr.next.val != "":

            steps -= 1
            self.curr = self.curr.next
            print(self.curr.val)

        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)