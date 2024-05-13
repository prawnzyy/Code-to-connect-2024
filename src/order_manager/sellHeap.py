import heapq

class sellHeap:
    
    def __init__(self):
        self.heap = heapq()

    def insert(self, TreeNode):
        self.heap.heappush(TreeNode)
        self.heap.heapify()
    
    def pop(self):
        item = self.heap.heappop()
        self.heap.heapify()
        return item
    
