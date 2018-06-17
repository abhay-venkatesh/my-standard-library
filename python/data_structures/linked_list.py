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
    head -> None
    tail -> None

    Case 3:
    [1]->[2]
    head -> [1]
    tail -> [2]
    prev -> [1]
    curr -> [2]
    """
    def delete(self, val):
        if self.head is None:
            return

        if self.head.val == val:
            if self.tail == self.head:
                self.tail = self.head.next
            self.head = self.head.next
            return

        if self.head.next is None:
            return

        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.val == val:
                if curr.next is None:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = curr.next

            prev = curr
            curr = curr.next

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(1)
    ll.delete(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    for node in ll:
        print(node.val)
