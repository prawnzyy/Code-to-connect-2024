import pandas as pd
from .heaps import InstrumentOrderBook

class ExchangeEngine:

    def __init__(self, report_manager):
        self.rm = report_manager
        self.instrument_heaps = {}

        # Create a instrument order book for each instrument
        instruments = self.rm.instruments.keys()
        for i_ in instruments:
            self.instrument_heaps[i_] = InstrumentOrderBook(i_, self.rm)
        
    def parse_order(self, curr_order):
        time, id_, instr, quantity, client, price, side = curr_order
        if side == 'SELL':
            check_4 : bool = self.is_valid_order(client, instr, quantity)
            if not check_4: # Fail check 4 -> return immediately, parse next row!
                self.reject_order(id_)
                return
            
        self.instrument_heaps[instr].parse_order(curr_order)

    def is_valid_order(self, client, instr, quantity):
        curr_pos = self.rm.client_state[client].get_position(instr)
        if quantity > curr_pos:
            return False
        return True

    def reject_order(self, id_):
        self.rm.add_rejected_order(id_, "REJECTED-POSITION CHECK FAILED")

