from check_pwd import check_pwd
import unittest

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertFalse("1234567891012345678910")


if __name__ == '__main__':
	unittest.main()
