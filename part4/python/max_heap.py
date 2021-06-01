import math

class MaxHeap():
    heap = []
    def __init__(self, init_heap = []):
        self.heap = init_heap.copy()

    def insert(self, x: int):
        if len(self.heap) == 0:
            self.heap.append(x)
        else:
            self.heap.append(x)
            self.sift_up(len(self.heap) - 1)
    
    def get_max(self):
        if len(self.heap) < 0:
            return None
        return self.heap[0];
    
    def extract_max(self):
        if len(self.heap) < 0:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.sift_down(0)
        return max_value
    
    def sift_up(self, leaf_i):
        parent_i = math.floor((leaf_i - 1) / 2)
        while 0 <= parent_i < len(self.heap) and self.heap[leaf_i] > self.heap[parent_i]:
            self.heap[parent_i], self.heap[leaf_i] = self.heap[leaf_i], self.heap[parent_i]
            leaf_i = parent_i
            parent_i = math.floor((leaf_i - 1) / 2)
    
    def sift_down(self, leaf_i):
        child_left_i, child_right_i = 2*leaf_i + 1, 2*leaf_i + 2
        while child_left_i < len(self.heap) and child_right_i < len(self.heap):
            if self.heap[leaf_i] <= self.heap[child_left_i]:
                if self.heap[child_right_i] > self.heap[child_left_i]:
                    self.heap[leaf_i], self.heap[child_right_i] = self.heap[child_right_i], self.heap[leaf_i]
                    leaf_i = child_right_i
                else:
                    self.heap[leaf_i], self.heap[child_left_i] = self.heap[child_left_i], self.heap[leaf_i]
                    leaf_i = child_left_i
            elif self.heap[leaf_i] <= self.heap[child_right_i]:
                if self.heap[child_left_i] > self.heap[child_right_i]:
                    self.heap[leaf_i], self.heap[child_left_i] = self.heap[child_left_i], self.heap[leaf_i]
                    leaf_i = child_left_i
                else:
                    self.heap[leaf_i], self.heap[child_right_i] = self.heap[child_right_i], self.heap[leaf_i]
                    leaf_i = child_right_i
            else:
                break
            child_left_i, child_right_i = 2*leaf_i + 1, 2*leaf_i + 2

    def print_heap(self):
        print(self.heap)

h1 = MaxHeap([7,6,5,4,3,2,1])
h1.print_heap()
h1.insert(100)
h1.print_heap()
print(h1.extract_max())
h1.print_heap()