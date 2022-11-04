class Solution(object):

    '''
    function: aboveBelow
    param1: unsorted collection of integers []
    param2: comparison integer
    returns: a hash/object/map/etc. with the keys "above" and "below" with 
             the corresponding count of integers from the list that are above or below the comparison value
    '''
    def aboveBelow(self, nums, target):
        result = {'above': 0, 'below': 0}

        for num in nums:
            if num < target:
                result['above'] += 1
            elif num > target:
                result['below'] += 1
        
        return result
    

    '''
    function: stringRotation
    param1: original string
    param2: positive integer rotation amount
    returns: a new string, rotating the characters in the original string to the right by the 
             rotation amount and have the overflow appear at the beginning
    '''
    def stringRotation(self, s, rotation):
        chars = list(map(str, s))
        n = len(chars)
        result = [""] * n

        if n == 0 or rotation == 0:
            return s

        if rotation > len(s):
            rotation = rotation % len(s)
        
        for i in range(n):
            if i + rotation >= n:
                curr = (i + rotation) - n
            else:
                curr = i + rotation

            result[curr] = chars[i]

        return "".join(result)




'''
function: main
creates an instance of solution and runs 2 provided test cases. Prints results
'''
def main():
    s = Solution()
    print(s.aboveBelow([1, 5, 2, 1, 10], 6))    
    print(s.stringRotation("MyString", 2))

if __name__ == "__main__":
    main()
        
    
