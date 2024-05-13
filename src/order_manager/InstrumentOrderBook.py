import buyHeap, sellHeap, report_manager

class InstrumentOrderBook:
    def __init__(self, id, reportManager):
        self.id = id
        self.buyHeap = buyHeap()
        self.sellHeap = sellHeap()
        self.market = [] * 10
        self.reportManager

    def getSellHeap(self):
        return self.sellHeap
    
    def getBuyHeap(self):
        return self.buyHeap
    
    def getMarket(self):
        return self.market
        