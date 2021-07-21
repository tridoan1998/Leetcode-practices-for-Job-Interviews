def maxProfit(self, prices: List[int]) -> int:
    '''
    prices = [7, 1, 5, 3 ,6 ,4]
    check for edge cases: empty array, negaive numbers, specil characters, or something like [1, 1, 1, 1, 1, 1, 1], what to return for these cases?
    use for loop to iterate through the prices array
    how do we know which is the lowest and highest?
    => use two variables to hold those value
    => iterate through the entire list, and update those two values accorrdingly.

    Time: O(N) average: iterate through every single elements in the array once.
    Space: O(1) because no additional data structures

    '''
    if len(prices) == 0 or len(prices) ==1:
        return 0
    else:
        #what value should we hold initially for these two variables?
        #set lowest to prices[0], not 0 because let's say [1, 2, 3, 4], then lowest is 1, not 0
        lowest = prices[0]
        highest = 0
        for i in range( len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if (prices[i] - lowest) > highest:
                higest = prices[i] - lowest
        return highest

def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    check for edge cases:
    length of array is one.
    return 0

    solve: multiple and store value in another array, multiply from left to right, another one from right to left,
    [1, 2, 3, 4 ] = [1, 1, 2, 6]
    [1, 2, 3, 4] = [24,12,4,1]
    Time: O(N), run the for loop once for every for loop run, therefore O(N) + O(N) = O(N)
    Space: O(N), because we are creating more array => more space in memory
    """
    arrayleft = [1]* len(nums)
    arrayright = [1] * len(nums)
    templeft = 1
    for i in range(len(nums)-1):
        templeft *= nums[i]
        arrayleft[i+1] = templeft
    nums.reverse() # build in fuction to reverse th list for the arrayright to multple and add in data
    templeft = 1
    for i in range(len(nums)-1):
        templeft *= nums[i]
        arrayright[i+1] = templeft
    arrayright.reverse()
    for i in range(len(nums)):
        nums[i] = arrayleft[i] * arrayright[i]
    return nums

def maxSubArray(self, nums: List[int]) -> int:
    """
    thoguht process:
    check for edge cases: [-2, -4, -5, -20] => return -2, maybe don't need to search through the list
    [1, 3, 5, 7 ,10, 15] => search through the entire list
    [-2, 1, -3, 4, 30]
    remind me of kardane althorim.
    currenmax to keep largest sum so far
    finalmax to keep largest of currenmax and finalmax
     [-2,1,-3,4,-1,2,1,-5,4]
     -2 + 1 = -1
     currmax = -1
     -1 - 3 = -4
     currmax = -1
     -4 + 4 = 0
     currmax = 0
     0 -1 = -1
     currmax = 0
     -1 + 2 = 1
     currmax = 1
     1 + 1 = 2      => finalmax, and wrong, we can set currMax to zero whenever we see zero, but does not work too because [-2, 1] = finalmax = -1, not zero.
     we can do
     currmax = 2
     2 -5 = -3
     -3 + 4 = 1

      currmax = -2+1 = 1 -3 = -2 +4 = 2 -1 = 1 + 2 = 3 + 1 = 4 -5 = -1 + 4 3
      finalmax 4
    """
    if len(nums) <= 1:
        return nums[0]
    else:
        currmax = 0
        finalmax = float('-inf')
        for i in range( len(nums)):
            currmax = max(nums[i], currmax + nums[i])
            if currmax > finalmax:
                finalmax = currmax
        return finalmax
