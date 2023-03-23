class LinkedList:
    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

        def __str__(self):
            return self.val

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        self.current = None

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):

        if not self.current:
            raise StopIteration()

        ret_val = self.current.val

        self.current = self.current.next
        return ret_val

    def __getitem__(self, idx):
        curr = self.first
        self._validate_idx(idx)

        for i in range(idx):
            curr = curr.next

        return curr.val

    def __len__(self):
        return self.count

    def _validate_idx(self, idx):
        if idx < 0 or idx > self.count - 1:
            raise IndexError()

    def append(self, val):
        node = self.Node(val)
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.first = node
            self.last = node
        self.count += 1

    def insert(self, idx, val):
        self._validate_idx(idx)

        curr = self.first

        for i in range(idx):
            curr = curr.next

        node = self.Node(val)
        node.next = curr.next
        curr.next = node

        self.count += 1

    def remove(self, idx):
        self._validate_idx(idx)

        if idx == 0:
            self.first = self.first.next

        else:
            curr = self.first

            for i in range(idx - 1):
                curr = curr.next

            curr.next = curr.next.next

        self.count -= 1
        if self.count == 0:
            self.last = None
            self.first = None

    def reverse(self):
        new_list = LinkedList()
        for val in self:
            new_node = self.Node(val)
            new_node.next = new_list.first
            new_list.first = new_node
            if new_list.last is None:
                new_list.last = new_node
            new_list.count += 1
        return new_list

    def __str__(self):
        return " -> ".join([n for n in self])


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.append("coconut")
    linked_list.append("kiwi")

    print(f"Linked list size: {len(linked_list)}")

    # print("Getting item at index 1...")
    # print(linked_list[1])
    #
    # print("First iteration")
    # print(linked_list)
    #
    # linked_list.insert(1, "orange")
    #
    # print("After adding orange")
    # print(linked_list)
    #
    # linked_list.remove(3)
    # print("After removing from idx 3")
    # print(linked_list)
    #
    # linked_list.remove(0)
    # print("After removing from idx 0")
    # print(linked_list)
    #
    # linked_list.remove(2)
    # print("After removing from idx 2")
    # print(linked_list)

    print(linked_list)

    print(linked_list.reverse())

