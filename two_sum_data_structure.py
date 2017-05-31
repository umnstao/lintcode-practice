class TwoSum(object):

    def __init__(self):
        # initialize your data structure here
        self.myList = []

    # Method 1
    def add(self, number):
        # Write your code here
        self.myList.append(number)

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        # O(n) time complexity, extra space
        mySet = {}
        for i in xrange(len(self.myList)):
            if self.myList[i] in mySet:
                return True
            mySet[value - self.myList[i]] = i
        return False
        
    def __init__(self):
        # initialize your data structure here
        self.myTable = {}
        self.myList = []


    # Method 2
    def add(self, number):
        # Write your code here
        self.myList.append(number)
        if number in self.myTable:
            self.myTable[number] += 1
        else:
            self.myTable[number] = 1
        
    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        # O(n) time complexity, no extra space
        for i in xrange(len(self.myList)):
            num1 = self.myList[i]
            num2 = value - num1
            if num2 == num1 and self.myTable[num2] > 1:
                return True
            if num2 != num1 and num2 in self.myTable:
                return True
        return False