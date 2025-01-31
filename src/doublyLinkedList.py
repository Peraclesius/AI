class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data) -> None:
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        self.head = current.next
        return

    def toList(self) -> list:
        ls = []
        current = self.head
        while current:
            ls.append(current.data)
            current = current.next
        return ls
