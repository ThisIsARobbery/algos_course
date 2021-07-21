import sys
class MaxHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
 
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def max_child(self, i):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] > self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def delete_max(self):
        if len(self.heap_list) == 1:
            return None
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        del self.heap_list[self.current_size]
        # *self.heap_list, _ = self.heap_list
        self.current_size -= 1
        self.sift_down(1)
        return root
    
    def print_heap(self):
        print(self.heap_list[1:])


heap = MaxHeap()
n = int(sys.stdin.readline())

for _ in range(n):
    inp = sys.stdin.readline().rstrip("\n")
    # print(inp)
    if inp == "ExtractMax":
        print(heap.delete_max())
    else:
        value = int(inp.split(" ")[1])
        heap.insert(value)
    # heap.print_heap()