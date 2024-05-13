import pandas as pd
from report_manager import ReportManager
from models import Client, Instrument

class MatchingEngine:

    def __init__(self, client_csv : str, instr_csv : str, order_csv : setattr):
        """Description
        Constructor for matching engine

        :param client_csv: File path for the csv with clients.
        :param instr_csv: File path for the csv with instruments.
        :param order_csv: File path for the csv with orders.
        """
        self.clients = self.create_client_states(client_csv)
        self.instruments = self.create_instrument_states(instr_csv)
        self.report_manager = ReportManager(self.clients, self.instruments)

    def translate_to_df(self, fp : str) -> pd.DataFrame:
        return pd.read_csv(fp)
    
    
    def create_client_states(self, client_csv : str) -> pd.DataFrame:
        client_states = {}

        def create_client(x):
            id_, currency_, position_check, rating_ = x
            currency_ = set(currency_.split(","))
            if id_ not in client_states:
                client_states[id_] = Client(id_, position_check, currency_, rating_)

        client_df = self.translate_to_df(client_csv)
        client_df.apply(create_client)
        return client_states    

    def create_instrument_states(self, instr_csv : str) -> pd.DataFrame:
        instrument_states = {}
        instrument_df = self.translate_to_df(instr_csv)

        def create_instruments(x):
            id_, curr_, ls_ = x
            if id_ not in instrument_states:
                instrument_states[id_] = Instrument(id_, ls_, curr_)

        instrument_df.apply(create_instruments)
        return instrument_df

    if __name__ == "__main__":
        print('test')