from collections import deque
class TreeNode:
    def __init__(self, price):
        self.price = price
        self.priorities = [deque()] * 10

    def getOrder(self):
        return self.price
    
    def getPrice(self):
        return self.price
    
    def getpriorties(self):
        return self.priorities
    
    def insert(self, order):
        rating = order.client.rating
        self.priorties[rating - 1].append(order)

    def removeFront(self, priority):
        return(self.priorities[priority - 1].pop())
    
    def __lt__(self, node):
        self.price > self.price
