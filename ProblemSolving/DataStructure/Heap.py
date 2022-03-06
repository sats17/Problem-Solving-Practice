class Heap:
    # Constructor to initialize the heap
    def __init__(self, heap):
        self.heap = heap
        self.size = heap.__len__()

    # Function to return the size of the heap
    def getSize(self):
        return self.size

if __name__ == "__main__":
    n = [5, 1, 2, 3, 4]
    h = Heap(n)
    print(h.getSize())