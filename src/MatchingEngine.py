import pandas as pd
from .report_manager import ReportManager
from .filtering_manager import FilteringManager
from .models import Client, Instrument
from .order_manager import ExchangeEngine

class MatchingEngine:

    def __init__(self, client_csv : str, instr_csv : str, 
                 order_csv : str, logger = print):
        """Description
        Constructor for matching engine

        :param client_csv: File path for the csv with clients.
        :param instr_csv: File path for the csv with instruments.
        :param order_csv: File path for the csv with orders.
        :param logger: Logger
        """
        self.clients = self.create_client_states(client_csv)
        self.instruments = self.create_instrument_states(instr_csv)
        self.report_manager = ReportManager(self.clients, self.instruments)
        self.filtering_manager = FilteringManager(self.clients, self.instruments, self.report_manager)
        self.exchange_manager = ExchangeEngine(self.report_manager)
        self.order_df = pd.read_csv(order_csv)
        self.filtered_orders = None
        self.logger = logger

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
        client_df.apply(create_client, axis=1)
        return client_states    

    def create_instrument_states(self, instr_csv : str) -> pd.DataFrame:
        instrument_states = {}
        instrument_df = self.translate_to_df(instr_csv)

        def create_instruments(x):
            id_, curr_, ls_ = x
            if id_ not in instrument_states:
                instrument_states[id_] = Instrument(id_, ls_, curr_)

        instrument_df.apply(create_instruments, axis=1)
        return instrument_states
    
    def filter_order_df(self):
        ret_df = self.filtering_manager.filter(self.order_df)
        self.filtered_orders = ret_df

    def run(self):
        self.logger("Applying filter to order chunk")
        self.filter_order_df()

        df = self.filtered_orders
        open_auction_df = df
        continuous_trading_df = df
        close_auction_df = df

        self.logger("Open Auction")
        

        self.logger("Continuous Trading")
        for _, order in continuous_trading_df.iterrows():
            self.exchange_manager.parse_order(order)

        self.logger("Close Auction")

        self.logger("Close Auction")
        self.report_manager.get_consolidated_reports()
        


        
