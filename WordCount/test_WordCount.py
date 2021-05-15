import unittest
import WordCount

class testCase(unittest.TestCase):
	
	def test1(self):
		self.assertEqual(WordCount.CountWords("a asdf asdf asdfl asdf asdf"),6)
	def test2(self):
		self.assertEqual(WordCount.CountWords("a1 1a 1 "),3)
	def test3(self):
		self.assertEqual(WordCount.CountWords("111.1 12.2 8 .a"),4)

if __name__ == '__main__':
	unittest.main()