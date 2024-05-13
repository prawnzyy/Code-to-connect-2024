from buyHeap import buyHeap
from sellHeap import sellHeap
from report_manager import ReportManager

class continuous:
    def __init__(self, ReportManager, InstrumentOrderbooks):
        self.reportManager = ReportManager
        self.iob = InstrumentOrderbooks

    def startTrade(self, order, df, clients):
        side = order[6]
        book = self.getInstrument(order[2]) #Check
        book.parseOrder(order)
        book.execute()

        