
<<<<<<< HEAD
class InstrumentOrderBook:
    def __init__(self, id, reportManager):
        self.id = id
        self.buyHeap = buyHeap()
        self.sellHeap = sellHeap()
        self.market = [[]] * 10
        self.reportManager = reportManager

    def getSellHeap(self):
        return self.sellHeap
    
    def getBuyHeap(self):
        return self.buyHeap
    
    def getMarket(self):
        return self.market
    
    def execute(self):

=======
>>>>>>> 8b4ddf6a9ebf9aafa962bc0787558dbfb01944dd
        