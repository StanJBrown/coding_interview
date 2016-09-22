
# todo type checking, and making sure the input has a comparison operator
# defined?


class MinHeap:
    def __init__(self):
        self.data = []

    def swap(self, x, y):
        self.data[x], self.data[y] = self.data[y], self.data[x]

    def heapifyUp(self, curr):
        parent = curr / 2
        curr_val = self.data[curr]
        parent_val = self.data[parent]

        while curr_val < parent_val and curr != 0:
            self.swap(curr, parent)
            curr = parent
            parent = curr / 2
            curr_val = self.data[curr]
            parent_val = self.data[parent]

        return

    def heapifyDown(self):
        # check both of the childern
        parent = 0
        end = len(self.data)

        while 2 * parent + 1 < end:
            child = 2 * parent + 1

            # check if right node exists and if it is larger then left
            if child + 1 < end and self.data[child] > self.data[child + 1]:
                child += 1

            # swap parent with child if parent is larger
            if self.data[parent] > self.data[child]:
                self.swap(parent, child)
                parent = child

            else:
                return

    def push(self, value):
        self.data.append(value)
        if len(self.data) > 1:
            self.heapifyUp(len(self.data) - 1)

    def pop(self):
        self.swap(0, -1)
        tmp = self.data.pop()
        self.heapifyDown()
        return tmp

    def peek(self):
        return self.data[0]


if __name__ == "__main__":
    values = [-1, -3, 2, 10, 3, 20233, 5, 7]
    test_heap = MinHeap()
    for val in values:
        test_heap.push(val)


    test_heap.pop()
    test_heap.pop()
    test_heap.push(-100)
    test_heap.push(222233444)

    while (len(test_heap.data) != 0):
        print "current heap      ", test_heap.data
        print "min value", test_heap.pop()





