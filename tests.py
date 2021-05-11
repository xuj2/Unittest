from check_pwd import check_pwd
import unittest

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertFalse("1234567891012345678910")

	def test2(self):
		self.assertFalse("1234567")

	def test3(self):
		self.assertFalse("A12345678")


if __name__ == '__main__':
	unittest.main()
