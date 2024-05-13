import buyHeap, sellHeap, report_manager

class InstrumentOrderBook:
    def __init__(self, id, reportManager):
        self.id = id
        self.buyHeap = buyHeap()
        self.sellHeap = sellHeap()
        self.marketBuy = [[]] * 10
        self.marketSell = [[]] * 10
        self.nodeTable = {}
        self.reportManager = reportManager

    def getSellHeap(self):
        return self.sellHeap
    
    def getBuyHeap(self):
        return self.buyHeap
    
    def getMarketBuy(self):
        return self.marketBuy
    
    def getMarketSell(self):
        return self.marketSell
    
    def insertNode(self, order):
        if order.price in self.nodeTable:
            self.nodeTable[order.price].insert(order)
        else:
            newPrice = order.price
            if order.side == 'Buy':
                node = self.buyHeap.insert(order)
            else:
                node = self.sellHeap.insert(order)
            self.nodeTable[newPrice] = node
            

    def parseOrder(self, order):
        if order.price == 'Market':
            client = report_manager.clients.get()
            if order.side == 'Buy':
                self.marketBuy[client].append(order)
            else:
                self.marketSell[client].append(order)
        else:
            if order.side == 'Buy':
                self.buyHeap.insert(order)
            else:
                self.sellHeap.insert(order)
                
        