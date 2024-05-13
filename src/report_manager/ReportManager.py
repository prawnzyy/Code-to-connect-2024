from utils import get_df
import pandas as pd
from models import Client, Instrument, RejectedOrder

class ReportManager:
    def __init__(self, client_df, instrument_df):
        self.clients = {}
        self.rejected_order = []
        self.accepted_orders = {}
        self.instruments = {}

        curr_clients = set(client_df['ClientID'])
        for c_ in curr_clients:
            self.client_positions[c_] = Client(c_)
        
        instruments = set(instrument_df['InstrumentID'])
        for i_ in instruments:
            self.instrument_stats[i_] = Instrument(i_)
    
    def add_rejected_order(self, order_id, rejection_reason):
        """Description
        Adds a rejected order to the report manager

        :param rejection_reason: Reason for rejection
        """
        self.rejected_orders.append(RejectedOrder(order_id, rejection_reason))

    def add_accepted_order(self, client_id, instrument_id, order_amount, order_price):
        """Description
        Adds a accepted order to the report manager.

        :param client_id: The client id we need to update.
        :param instrument_id: The instrument to update
        :param order_amount: The amount ordered by the client.
        """

        # Update client hm
        if client_id not in self.clients: 
            self.clients[client_id] = Client(client_id)
        
        # Update instrument hm
        if instrument_id not in self.instruments:
            self.instruments[instrument_id] = Instrument(instrument_id)
        
        # Update client position
        curr_client = self.clients[client_id]
        curr_client.update_position(instrument_id, order_amount)

        # Update instrument history
        curr_instrument_report = self.instruments[instrument_id]
        curr_instrument_report.add_trade(order_price, order_amount)

    def get_client_position(self, client_id, instrument_id):
        """Description
        Gets a client's position in a particular instrument.

        :param client_id: The id of the client in interest.
        :param instrument_id: The id of the instrument in interest.
        """
        return self.clients[client_id].get_position(instrument_id)
        
    
    def generate_exchange_report(self) -> pd.DataFrame:
        """Description
        Returns the exchange report.
        """
        return pd.DataFrame({
            'OrderID' : [x.get_id() for x in self.rejected_order],
            'RejectionReason' : [x.get_reason() for x in self.rejected_order]
        })
    
    def generate_client_report(self) -> pd.DataFrame:
        """Description
        Returns the client report.
        """

        # Start with a empty dataframe.
        client_report = pd.DataFrame({'ClientID' : [],
                                    'InstrumentID' : [], 
                                    'NetPosition' : []})
        
        # Update via concatenating client reports
        for c_ in self.clients:
            curr_report = c_.get_client_statistics()
            client_report.concat(curr_report)

        return client_report
    
    def generate_instrument_report(self) -> pd.DataFrame:
        """Description
        Returns the instrument reports
        """

        instrument_report = pd.DataFrame({
            "InstrumentID" : [],
            "OpenPrice" : [],
            "ClosePrice" : [],
            "TotalVolume" : [],
            "VWAP" : [],
            "DayHigh" : [],
            "DayLow" : []
        })
        
        # Update report
        for i_ in self.instruments:
            curr_is = i_.get_instrument_statistics()
            instrument_report.concat(curr_is)
        return instrument_report
    
    def get_consolidated_reports(self, output_dir="../../output"):
        """Description
        Returns the consolidated reports needed.

        :param output_dir: The output directory to write into.

        :return: A dictionary with the reports.
        """
        exchange_report = self.generate_exchange_report()
        client_report = self.generate_client_report()
        instrument_report = self.generate_instrument_report()
        reports = {'output_exchange_report': exchange_report,
                   'output_client_report' : client_report,
                   'instrument_report' : instrument_report}
        for k, v in reports.items():
            v.to_csv("output_{}.csv".format(k))
