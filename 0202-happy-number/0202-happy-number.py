class Solution:
    # function that computes the square of the number
    def extractSquare(self,value):
        squareValue = 0
        while value > 0:
            num = value % 10
            squareValue = squareValue + num * num
            value = value // 10

        return squareValue
    
    def isHappy(self, n: int) -> bool:
        # we are considering a set so that we store that values that we encounter during the finding of sums
        setOfValues = set()
        # loop has to run until n becomes 1
        while n != 1:
            newValue = self.extractSquare(n)
            n = newValue
            # if value already present in the set , it enters a cycle hence we need to return 
            if newValue in setOfValues:
                return False
            # if not found in the set, we need to add it to the set
            else:
                setOfValues.add(newValue)

        return True



        
        