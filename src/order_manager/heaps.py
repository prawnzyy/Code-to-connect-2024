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
            if self.rating > other.rating:
                return True
            if self.rating == other.rating:
                return self.time < other.time
        return False
                
class BuyHeap:
    def __init__(self):
        self.heap = []

    def add_heap(self, order):
        heapq.heappush(self.heap, order)
    
    def pop_heap(self):
        return heapq.heappop(self.heap)
    
class SellHeap:
    def __init__(self):
        self.heap = []

    def add_heap(self, order):
        heapq.heappush(self.heap, order)

    def pop_head(self):
        return heapq.heappop(self.heap)
    
class InstrumentOrderBook:
    def __init__(self):
        self.buy_heap = BuyHeap()
        self.sell_heap = BuyHeap()
    
    def add_order(self, order):
        pass

    def pop_order(self, order):
        pass