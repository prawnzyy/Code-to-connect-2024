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
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def peek_heap(self):
        return self.heap[0]
    
class SellHeap:
    def __init__(self):
        self.heap = []

    def add_heap(self, order):
        heapq.heappush(self.heap, order)

    def pop_head(self):
        return heapq.heappop(self.heap)
class InstrumentOrderBook:
    def __init__(self, id, rm):
        self.id = id
        self.buy_heap = BuyHeap()
        self.sell_heap = BuyHeap()
        self.rm = rm
        self.market_buy = BuyHeap()
        self.market_sell = BuyHeap()
    
    def add_order(self, order):
        if order.price == 'MARKET':
            if order.side == "BUY":
                self.market_buy.append(order)
            else:
                self.market_sell *= -1
                self.market_sell.append(order)
        else:
            if order.side == 'BUY':
                self.buy_heap.add_heap(order)
            else:
                self.sell_heap.add_heap(order)

    def execute(self):
        """Description
        Executes and matches both buy and sell heap together.
        """

        # Clear market orders first
        while not self.market_buy.is_empty() and not self.sell_heap.is_empty() and self.market_buy >= self.sell_heap:
            best_buy = self.market_buy.pop_heap()
            best_sell = self.sell_heap.pop_heap()
            execution_price = best_sell
            self.rm.add_accepted_order(best_buy.cli, self.id, 
                                       1, execution_price)
            self.rm.add_accepted_order(best_sell.cli, self.id, 
                                    -1, execution_price)
            
        while not self.market_sell.is_empty() and self.buy_heap.is_empty() and self.market_sell[0] <= self.buy_heap:
            best_buy = self.buy_heap.pop_heap()
            best_sell = self.market_sell.pop_heap()
            execution_price = best_buy
            self.rm.add_accepted_order(best_sell.cli, self.id, 
                                       -1, execution_price)
            self.rm.add_accepted_order(best_buy.cli, self.id, 
                                    1, execution_price)

        # Match heaps together
        while not self.buy_heap.is_empty() and not self.sell_heap.is_empty() and self.buy_heap.peek_heap() >= self.sell_heap.peek_heap():
            best_buy = self.buy_heap.pop_heap()
            best_sell = self.sell_heap.pop_heap()
            execution_price = best_buy
            if best_buy.time > best_sell.time:
                execution_price = best_sell
            # Executes
            self.rm.add_accepted_order(best_buy.cli, self.id, 
                                       1, execution_price)
            self.rm.add_accepted_order(best_sell.cli, self.id, 
                                       -1, execution_price)



    