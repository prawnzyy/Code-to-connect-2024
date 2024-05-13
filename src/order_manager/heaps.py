import heapq

class OrderNode:
    def __init__(self, order, cli_rating):
        self.time, self.order_id, self.instr, self.quantity, \
            self.cli, self.price, self.side = order
        self.rating = cli_rating
    
    def __lt__(self, other):
        if self.price > other.price:
            return True
        if self.price == other.price:
            if self.price <= other.price:
                return

        
        return False

                
class BuyHeap:
    def __init__(self):
        self.heap = []

    def add_heap(self, order):
        heapq.heappush(self.heap, order)
    
    def pop_heap(self):
        return heapq.heappop(self.heap)