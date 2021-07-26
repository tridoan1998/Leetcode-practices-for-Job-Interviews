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

def maxProduct(self, nums: List[int]) -> int:
    pre_max = nums[0]
    pre_min = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]
    ans = nums[0]

    #run the for loop from value index 1 to the end
    for i in nums[1:]:
        #compare it with max(blablabla, i) => this is to satisfy the continigoue subarray requirement
        curr_max = max(max(pre_max*i, pre_min*i), i)
        curr_min = min(min(pre_max*i, pre_min*i), i)
        pre_max = curr_max
        pre_min = curr_min
        ans = max(ans, curr_max)
    return ans


    """
    thought process => brainstorm the problem, don't jump straight into code, the more brainstorm, the more ideas will come across our mind.
    step 0 (edge cases):
    nums = [2,3,-2,4]
    2 * 3 = 6
    6 * -2 = -12
    thinking of dynamic programming where we keep track of the current value and update it whenever nessescary.
    we need temp variable to hold the current mul:
    currmul: 2 * 3 = 6
    6 * -2 = -12
    -12 * 4 = - 48
    another variable to keep highestpositive, and lowestnegative
    if currmul< 0:
        lowestnegative = currmul
    if currmul >= 0:
        highestpositive = currmul

    return highestpositive


    observation:
    currmul = 6 > -12, keep 6 => how do we do this?
    solve:
    [] =>
    [one element] =>
    [two elements] =>
    [all positive] => return the whole array
    [-1 , -2, -2, -6] => check all elements
    [1, 2, 5, 0, -1, 4, -6]
    final_array = [] => has to be non empty => insert it with some temporary => which number should we choose => the first element in the array ofc
    final_array.append(nums[0])
    use loop to iterate through the entire array => linear time O(N), can't have better time complexity than this because every elements needed to be access in this case
    for i in range(len(nums)):
        #at every itertion, what do we do?
    Time complexity:
    Space cpmplexity:
    """

def findMin(self, nums: List[int]) -> int:
    """
    step 0: check for edge cases:
        [] or [one element] => return -1
    given: sorted increasing order [-5, -3 , 0, 4, 7, 30]
    rotated between 1 and n time
    unique elements => does not matter negative, zero, or positive
    [5, 4, 6, 1, 2 ] => what to do with this case??? not gonna happends because given

    find pivot point maybe???
    use BST to find pivot???
    [3,4,5,1,2]
    search until we find the pivot index,
    the elemnt at that pivot index is the minimum, remember to check for outofounce array index too****
    how to find the pivot=> we search => linear => search every element until we find nums[i-1] > nums[i] and nums[i] < nums[i+1] => return nums[i] as pivot point(make sure i+1 is not outofbounce of the array)
    time: O(N) for linear search
    use binary search for better time O(logN)
    space: O(1) no additional array needed
    because sorted array so we can use BST, otherwise can't!!
    recursively or iteratively => recursively
    steps for bst:
    find the middle index, check if middle index satisfy nums[i-1] > nums[i] and nums[i] < nums[i+1], if it is then return nums[middle], else go recursively call the function again, passing middle-1 as the most left element, and do the same thing with middle+1 as the most right element
    base case for recursive: while left < right
    if greater than target,
    4,5,6,7,8, 9, 10, 11, 0,1,2
    middle is 9, how do we know which way left or right to go?
    look at left most and right most, 4 < 9 => the left side is already in order and not rotated, right side suppose to be greater than 9 but we see 2 => check right side

    """
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) ==2:
        if nums[0] <nums[1]:
            return nums[0]
        return nums[1]
    else:
        #[1, 2, 3, 4, 5,]
        left, right = 0, len(nums)-1
        while left < right:
            middle = int(left + ((right-left)/2))
            if nums[middle] > nums[middle-1] and nums[middle+1] < nums[middle]:
                return nums[middle+1]
            if nums[middle] < nums[middle-1] and nums[middle] < nums[middle+1]:
                return nums[middle]
            else:
                if nums[0] < nums[middle]:
                    left = middle+1
                if nums[0] > nums[middle]:
                    right = middle-1
        return nums[0]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(self, head: ListNode) -> ListNode:
    """
    edge cases:
    empty linkedlist => return None
    one elemnt => return that element
    does not matter what the value in the linkedlist hold, duplicate are okay too.
    linkedlist has a node, which has val and next
    we use two pointers, one point at the curr, one point at next node.

"""
    prev, curr = None, head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(self, head: ListNode) -> bool:
    dictionary = {}
    """
    key/value hashmap
    store head value in the dictionary


    """
    while head:
        if head in dictionary:
            return True
        dictionary[head] = True
        head = head.next
    return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    while l1:
        curr.next = l1
        l1 = l1.next
        curr = curr.next
    while l2:
        curr.next = l2
        l2 = l2.next
        curr = curr.next
    return dummy.next


def isAnagram(self, s: str, t: str) -> bool:
    """
    first loop
    if we first see the key, mark it with 1
    second loop
    run the t string, if the char in t existed in counter, minutes 1 from their value

    finally check the status of the counter dictionary see if any value is still 1 => return false else return true


    counter  key value
              a    1



    """

    """
    a_string = "cba"
sorted_characters = sorted(a_string) Sort string alphabetically and return list.
a_string = "". join(sorted_characters) Combine list elements into one string.
print(a_string)
    """
    if len(s) != len(t):
        return False
    else:
        s_sorted_character = sorted(s)
        t_sorted_character = sorted(t)
        print(s_sorted_character)
        print(t_sorted_character)
        for i in range(len(s_sorted_character)):
            if s_sorted_character[i] != t_sorted_character[i]:
                return False
        return True


def isAnagram(self, s: str, t: str) -> bool:
    """
    first loop
    if we first see the key, mark it with 1
    second loop
    run the t string, if the char in t existed in counter, minutes 1 from their value

    finally check the status of the counter dictionary see if any value is still 1 => return false else return true


    counter  key value
              a    1



    """

    """
    a_string = "cba"
sorted_characters = sorted(a_string) Sort string alphabetically and return list.
a_string = "". join(sorted_characters) Combine list elements into one string.
print(a_string)
    """
    if len(s) != len(t):
        return False
    else:
        counter =[0]* 26
        print(counter)
