import pandas as pd

class Matching:
    def __init__(self, report_manager):
        self.rm = report_manager
        self.instrument_heaps = {}

    def match_orders(order_df : pd.DataFrame):
        buy_orders = order_df[order_df['Side'] == 'Buy']
        sell_orders = order_df[order_df['Side'] == 'Sell']
        sell_orders.sort_values(by=['Time'], axis=0, ascending=True, inplace=True)
        buy_orders.sort_values(by=['Time'], axis=0, ascending=True, inplace=True)
    

