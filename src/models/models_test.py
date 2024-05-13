from Client import Client
from Instrument import Instrument
from Order import Order
from RejectedOrder import RejectedOrder
import unittest

class TestClient(unittest.TestCase):
    """
    Description: Check getter methods are working
    """
    def test_getters(self):
        first = Client("Test", True, set({'USD', "JPY"}), 2)
        self.assertEqual(first.get_rating(), 2)
        self.assertEqual(first.get_position_check(), True)
        self.assertTrue(first.check_valid_currency("USD"))

    """
    Description: Check the update_instrument
    """
    def test_update_instruments(self):
        first = Client("Test", True, set({'USD', "JPY"}), 2)
        first.update_position(1, 100)
        self.assertEqual(first.get_position(1), 100)
        first.update_position(1, 100)
        self.assertEqual(first.get_position(1), 200)

class TestInstrument(unittest.TestCase):
    
    def test_getters(self):
        first = Instrument("SIA", 100 , 'SGD')
        self.assertEqual(first.get_currency(), 'SGD')