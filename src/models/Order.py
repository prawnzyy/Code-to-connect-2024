class Order:
    """
        Description: An instance of an order
    """
    def __init__(self, time, orderID, instrument, quantity, client, price, side):
        self.time = time
        self.orderID = orderID
        self.instrument = instrument
        self.quantity = quantity
        self.client = client
        self.price = price
        self.side = side

    def getTime(self):
        return self.time
    
    def getOrderID(self):
        return self.orderID
    
    def getInstrument(self):
        return self.instrument
    
    def getQuantity(self):
        return self.quantity
    
    def getClient(self):
        return self.client
    
    def getPrice(self):
        return self.price
    
    def getSide(self):
        return self.side

