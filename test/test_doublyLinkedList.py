from doublyLinkedList import DoublyLinkedList


def test_append():
    ll = DoublyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    assert ll.toList == [1, 2, 3, 4]

