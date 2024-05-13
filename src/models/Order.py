class Order:
    """
    Description: This class represents an order
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
    
    def breakdown(self):
        orders = []
        for i in range(self.quantity):
            orders.append(Order(self.time, self.orderID, self.instrument, 1, self.client, self.price, self.side))
        return orders

