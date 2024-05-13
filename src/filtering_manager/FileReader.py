import csv
from pathlib import Path
import os
import pandas as pd

def filter_lot(x, instruments):
    instrument = instruments[x['Instrument']]
    #return instrument.is_valid_lot_size(x[])

def filter_currency(x, clients, instruments):
    instrument = instruments[x['Instrument']]
    currency = clients[x['Client']]

    return (instrument['Currency'] in currency.split(","))

def filter_condition(order_path, clients, instruments):
    order_df = pd.read_csv(order_path)

    #Check 1
    valid_instruments = set(instruments['InstrumentID'])
    order_df = order_df[order_df['Instrument'] in valid_instruments]

    #Check 2
    order_df = order_df.apply(lambda x : filter_currency(x, clients, instruments))

    #Check 3
    order_df = order_df.apply(lambda x : filter_lot(x, instruments))
    return order_df

def retrieve_client():
    Client_data = []
    Client_header = ''
    print(Path.cwd())
    # Note to fix the path 
    with open(str(Path.cwd()) + "\Code-to-connect-2024\C2C-2024-DataSet\DataSets\example-set\input_clients.csv", 'r') as file:
        csvreader = csv.reader(file)
        client_header = next(csvreader)
        for row in csvreader:
            Client_data.append(row)
    return Client_data

def retrieve_instrument():
    Instrument_data = []
    Instrument_header = ''
    with open(str(Path.cwd()) + "\Code-to-connect-2024\C2C-2024-DataSet\DataSets\example-set\input_instruments.csv", 'r') as file:
        csvreader = csv.reader(file)
        Instrument_header = next(csvreader)
        for row in csvreader:
            Instrument_data.append(row)
    return Instrument_data

def retrieve_order():
    Order_data = []
    Order_header = ''
    with open(str(Path.cwd()) + "\Code-to-connect-2024\C2C-2024-DataSet\DataSets\example-set\input_orders.csv", 'r') as file:
        csvreader = csv.reader(file)
        Order_header = next(csvreader)
        for row in csvreader:
            Order_data.append(row)
    return Order_data

def clean_order(orders, instruments, clients):
    index = 0
    while index < len(orders):
        order_instrument = orders[index][2]
        order_client = orders[index][1]
        instrument_ids = [instrument[0] for instrument in instruments]
        #Check 1
        if order_instrument not in [instrument[0] for instrument in instruments]:
            print(orders[index], "A")
            orders = orders[:index] + orders[index + 1:]
            continue
        #Check 2
        client_ids = [client[0] for client in clients]
        if instruments[instrument_ids.index(order_instrument)][1] not in clients[client_ids.index(orders[index][4])][1].split(","): 
            print(orders[index], "B")
            orders = orders[:index] + orders[index + 1:]
            continue
        #Check 3
        if int(orders[index][3]) % int(instruments[instrument_ids.index(order_instrument)][2]) != 0:
            print(orders[index], "C")
            orders = orders[:index] + orders[index + 1:]
            continue
        index += 1

clean_order(retrieve_order(), retrieve_instrument(), retrieve_client())
