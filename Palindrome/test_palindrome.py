import unittest
import palindrome

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(palindrome.isPalindrome("racecar"),True)
	def test2(self):
		self.assertEqual(palindrome.isPalindrome("a1b33b1a"),True)
	def test3(self):
		self.assertEqual(palindrome.isPalindrome("racecar dad mom"),False)

if __name__ == '__main__':
	unittest.main()