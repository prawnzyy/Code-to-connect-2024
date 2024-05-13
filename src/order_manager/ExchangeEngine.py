import pandas as pd
from InstrumentOrderBook import InstrumentOrderBook

class ExchangeEngine:
    def __init__(self, report_manager):
        self.rm = report_manager
        self.instrument_heaps = {}

        # Create a instrument order book for each instrument
        instruments = self.rm.instruments.keys()
        for i_ in instruments:
            self.instrument_heaps[i_] = InstrumentOrderBook(i_, self.rm)
        
    def parse_order(self, curr_row):
        time, orderid, instrument, quantity, client, price, side = curr_row


    def is_valid_order(self, order):

        pass

    def reject_order(self, order):
        pass

