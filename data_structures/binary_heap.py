
# todo type checking, and making sure the input has a comparison operator
# defined?


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify(self):
        i = 0
        while (i < len(self.data) - 1):
            if (self.data[i] > self.data[i+1]):
                self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                i = 0
                continue
            i += 1

    def push(self, value):
        self.data.append(value)
        self.heapify()

    def pop(self):
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        tmp = self.data.pop()
        self.heapify()
        return tmp

    def peek(self):
        return self.data[0]


if __name__ == "__main__":
    values = [-1, -3, 1, 2, 10, 3, 20233, 1, 5, 7]
    test_heap = MinHeap()
    for val in values:
        test_heap.push(val)

    test_heap.pop()
    test_heap.pop()
    test_heap.push(-100)
    test_heap.push(222233444)

    while (len(test_heap.data) != 0):
        print "current heap      ", test_heap.data
        print "minimum value     ", test_heap.pop()
