import heapq

class buyHeap:
    
    def __init__(self):
        self.heap = heapq()

    def insert(self, TreeNode):
        self.heap.heappush(TreeNode)
        self.heap.heapify()
    
    def pop(self):
        self.heap.heappop()
        self.heap.heapify()