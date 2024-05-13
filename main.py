
from src import MatchingEngine

if __name__ == "__main__":
    engine = MatchingEngine("./C2C-2024-DataSet/DataSets/example-set/input_clients.csv",
                            "./C2C-2024-DataSet/DataSets/example-set/input_instruments.csv",
                            "./C2C-2024-DataSet/DataSets/example-set/input_orders.csv")
    engine.run()