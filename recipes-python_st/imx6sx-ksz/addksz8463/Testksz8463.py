import unittest
from ksz8463 import ksz

class Testksz8463(unittest.TestCase):
      #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.ksz = ksz()
  #Each test method starts with the keyword test_
  def test_spi(self):
      self.assertEqual(self.spitest(), "0X8443")
if __name__ == "__main__":
  unittest.main()