
def CountWords(string):
    total = 1
    for i in range(len(string)):
        if(string[i] == ' ' or string == '\n' or string == '\t'):
            total = total + 1
    return total


def testCase():
	def test_one(self):
		assert CountWords("a asdf asdf asdfl asdf asdf")==6
	def test_two(self):
		assert CountWords("a1 1a 1 ")==3
	def test_three(self):
		assert CountWords("111.1 12.2 8 .a")==4