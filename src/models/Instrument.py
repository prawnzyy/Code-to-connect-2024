import pandas as pd

class Instrument:
    """Description
    This class represents a instrument.
    """
    def __init__(self, name):
        self.opening = None
        self.closing = None
        self.instrument_name = name
        self.trades = {'price' : [], 'volume' : []}
        self.final_trades = pd.DataFrame(self.trades)
    
    def set_opening(self, price):
        # Def. programming
        if self.opening is None:
            self.opening = price
    
    def set_closing(self, price):
        # Def. programming
        if self.closing is None:
            self.closing = price

    def get_opening(self):
        return self.opening

    def get_closing(self):
        return self.closing
    
    def add_trade(self, price, vol):
        self.trades['price'].append(price)
        self.trades['volume'].append(vol)
    
    def reformat_trades_for_calculation(self) -> pd.DataFrame:
        self.final_trades = pd.DataFrame(self.trades)
    
    def get_total_vol(self):
        return sum(self.final_trades['volume'])
    
    def get_high_low(self):
        """Description
        Gets high, low price for current instrument.
        
        :return: Low price, high price in that order.
        """
        return min(self.final_trades['price']), max(self.final_trades['price'])

    def get_vwap(self):
        """Description
        Calculate VWAP for the instrument.
        """
        prices = abs(self.final_trades['price'])
        vol = self.final_trades['volume']
        return (prices * vol) / sum(vol)

    def get_instrument_statistics(self):
        """Description
        Generates descriptive report for the current instrument.

        :return: opening, closing, total trading vol, low, high, VWAP in that order.
        """
        opening = self.get_opening()
        closing = self.get_closing()
        t_vol = self.get_total_vol()
        low, high = self.get_high_low()
        vwap = self.get_vwap()
        
        df = pd.DataFrame({
            "InstrumentID" : self.name,
            "OpenPrice" : opening,
            "ClosePrice" : closing,
            "TotalVolume" : t_vol,
            "VWAP" : vwap,
            "DayHigh" : high,
            "DayLow" : low
        })

        return df