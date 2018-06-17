class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = None
        if val is not None:
            self.val = val 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
     
    def append(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
    """
    Case 1:
    None 
    
    Case 2:
        LinkedList: 
            [1]->None
            head -> [1]
            tail -> [1]
    
    case 3: 
    
    
    """        
    def delete(self, val):
        curr = self.head
        prev = self.head
        while curr is not None:
            if curr.val == val:
                if curr == self.head:
                    self.head = None 
                    self.tail = None
                elif curr.next is None:
                    
                    
                    
            curr = curr.next
    
    def __iter__(self):
        curr = self.head 
        while curr is not None:
            yield curr
            curr = curr.next
