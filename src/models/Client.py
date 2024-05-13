import pandas as pd

class Client:
    def __init__(self, name, position_check : bool, currency : set, rating : int):
        self.name = name
        self.position_check = position_check
        self.accepted_currency = currency
        self.rating = rating
        self.positions = {}

    def get_rating(self):
        return self.rating

    def get_position_check(self):
        return self.position_check
    
    def check_valid_currency(self, currency : str):
        return currency in self.accepted_currency
    
    def update_position(self, instrument_id, position_delta):
        """Description
        Updates the client's current position for a given instrument.

        :param instrument_id: The id of the instrument to be updated.
        :param position_delta: The amount to update that particular position by.
        """
        if instrument_id not in self.positions:
            self.positions[instrument_id] = 0
        self.positions[instrument_id] += position_delta
    
    def get_position(self, instrument_id):
        """Description
        Get the client's current position for a particular instrument.

        :param instrument_id: The id of the instrument to be updated.
        """
        return self.positions[instrument_id]
    
    def get_client_statistics(self):
        """Description
        Returns the client's statistics.
        """
        positions_sum = [sum(x) for x in self.positions.values()]
        c_id = [self.name for _ in range(len(self.positions.keys()))]
        reformat_positions = {'ClientID' : c_id,
                                'InstrumentID' : self.positions.keys(), 
                              'NetPosition' : positions_sum}
        return pd.DataFrame(reformat_positions)