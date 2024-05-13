from .buyHeap import buyHeap
from .sellHeap import sellHeap
from .TreeNode import TreeNode

class InstrumentOrderBook:
    def __init__(self, id, reportManager):
        self.id = id
        self.bh = buyHeap()
        self.sh = sellHeap()
        self.marketBuy = []
        self.marketSell = []
        self.price_cache = {}
        self.rm = reportManager
        self.cache = {}

    def getSellHeap(self):
        return self.sh
    
    def getBuyHeap(self):
        return self.bh
    
    def getMarketBuy(self):
        return self.marketBuy
    
    def getMarketSell(self):
        return self.marketSell

    def is_in_cache(self, price):
        if price not in self.price_cache:
            return False
        else:
            return True
            
    def parseOrder(self, order):
        clients = self.rm.client_state
        time, _, _, cli_id, price, side = order
        if price == 'MARKET':
            if side == 'BUY':
                self.marketBuy.append((clients[cli_id].ratings, time, order))
            else:
                self.marketSell.append((clients[cli_id].ratings, order))
        else:
            is_cached : bool = self.is_in_cache(price)
            if is_cached: # Check cache for direct insert
                tree_node = self.price_cache[price] 
                tree_node.insert(order)
            else:
                if side == 'BUY':
                    tree_node = self.bh.insert(order)
                elif side == 'SELL':
                    tree_node = self.sh.insert(order)
                self.price_cache[price] = tree_node # Add to cache

        self.execute()

    def execute(self):
        self.marketBuy = sorted(self.marketBuy, lambda x : (-x[0], x[1]))
        self.marketSell = sorted(self.marketSell, lambda x : (-x[0], x[1]))
        while len(self.marketBuy) > 0 and self.sh.get_size() > 0:
            market_buy = self.marketBuy.pop(0)
            seller_ = self.sh.pop()
            execution_price = seller_.price
            execution_amount = min(seller_.quantity, market_buy.quantity)
            self.rm.add_accepted_order(market_sell.client, self.id, 
                                       -execution_amount, execution_price)
            
            rem = market_buy.quantity - execution_amount
            if rem > 0:
                market_buy.quantity -= execution_amount
                self.marketBuy.append(market_buy)

            rem_ = seller_.quantity - execution_amount
            if rem_ > 0:
                seller_.quantity -= execution_amount
        
        while len(self.marketSell) > 0 and self.bh.get_size() > 0:
            market_sell = self.marketSell.pop(0)
            buyer_ = self.bh.pop()
            execution_price = buyer_.price
            execution_amount = min(buyer_.quantity, market_sell.quantity)
            self.rm.add_accepted_order(market_sell.client, self.id, 
                                       -execution_amount, execution_price)
