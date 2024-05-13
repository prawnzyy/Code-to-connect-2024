import pandas as pd

class Client:
    def __init__(self, name):
        self.name = name
        self.positions = {}
    
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
        reformat_positions = {'ClientID' : [self.name * len(self.positions.keys())],
                                'InstrumentID' : self.positions.keys(), 
                              'NetPosition' : self.positions.values()}
        return pd.DataFrame(reformat_positions)