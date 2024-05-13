class FilteringManager:
    def __init__(self, clients, instruments):
        self.clients = clients
        self.instruments = instruments

    def filter(self, order_df_):
        order_df = order_df_.copy()
        def filter(x):
            time, id_, instrument_id, quantity, client, _, _ = x

            curr_instrument = self.instruments[instrument_id]
            curr_client = self.clients[client]
            check_1 : bool = instrument_id in self.instruments.keys()
            check_2 : bool = curr_client.check_valid_currency(curr_instrument.get_currency())
            check_3 : bool = curr_instrument.is_valid_lot_size(quantity)

            return check_1 and check_2 and check_3
        
        order_df['criterion'] = order_df.apply(filter, axis=1)
        order_df = order_df[order_df['criterion'] == True]
        order_df.drop('criterion', axis=1, inplace=True)
        return order_df
    
