class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_end(self, data):
        if self.head is None:
           new_node = Node(data)
           new_node.prev = None
           self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None


    def print_forward(self):
            if self.head is None:
                print("Linked list is empty")
                return

            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
                itr = itr.next
            print(llstr)


    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next


        llstr = ''
        while itr.prev:
            llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev

        if itr.prev is None:
            llstr += str(itr.data)

        print(llstr)



if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange", "watermelon"])
    ll.print_forward()
    ll.print_backward()

