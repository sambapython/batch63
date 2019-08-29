from app import add
import unittest
class AddTest(unittest.TestCase):
	@classmethod
	def tearDownClass(cls):
		print("this is teardown class method")
		cls.user=None
	def setUp(self):
		print("this is setup")
	def tearDown(self):
		print("this is tearDown")
	def test_10_20(self):
		print("this is test_10_20")
		print(self.user)
		act=add(10,20)
		exp=30
		self.assertEqual(act,exp,"test_10_20 failed")
	def test_str1_20(self):
		print("this istest_str1_20 ")
		print(self.user)
		act=add("str1",20)
		exp=None
		self.assertEqual(act,exp,"test_str1_20 failed")
	def test_10_str2(self):
		print("this test_10_str2 ")
		print(self.user)
		act=add(10,"str2")
		exp=None
		self.assertEqual(act,exp,"test_10_str2 failed")
	@classmethod
	def setUpClass(cls):
		cls.user="samba"
		print("this is setUp class method")