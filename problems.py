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
