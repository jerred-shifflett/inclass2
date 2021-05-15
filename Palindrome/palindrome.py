
#split the string in half and then compare both of those halfs
#comparing the head to the tail iteratively.
def isPalindrome(string):
 
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            return False
    #we have a palindrome
    return True
