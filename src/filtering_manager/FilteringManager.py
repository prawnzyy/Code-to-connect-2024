import pandas as pd

class FilteringManager:
    def __init__(self, clients, instruments, rm):
        self.clients = clients
        self.instruments = instruments
        self.rm = rm

    def filter(self, order_df_ : pd.DataFrame) -> pd.DataFrame:
        """Description
        Filters chunk of orders based on conditions given in paper.

        :return: Filtered dataframe
        """
        order_df = order_df_.copy()
        def filter(x):
            _, id_, instrument_id, quantity, client, _, _ = x

            curr_instrument = self.instruments[instrument_id]
            curr_client = self.clients[client]
            check_1 : bool = instrument_id in self.instruments.keys()
            if check_1 == False:
                self.rm.add_rejected_order(id_, "REJECTED-INSTRUMENT NOT FOUND")
                return False
            check_2 : bool = curr_client.check_valid_currency(curr_instrument.get_currency())
            if check_2 == False:
                self.rm.add_rejected_order(id_, "REJECTED-MISMATCH CURRENCY")
                return False
            check_3 : bool = curr_instrument.is_valid_lot_size(quantity)
            if check_3 == False:
                self.rm.add_rejected_order(id_, "REJECTED-INVALID LOT SIZE")
                return False
            return check_1 and check_2 and check_3
        
        order_df['criterion'] = order_df.apply(filter, axis=1)
        order_df = order_df[order_df['criterion'] == True]
        order_df.drop('criterion', axis=1, inplace=True)
        return order_df
    
