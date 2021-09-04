


def dfs(self, visited, v):
	visited.append(v)
	v.isVisited = True
	for childnode in graph[v]:
		if !childnode.isVisited:
			dfs(self, visited, childnode)


def miniumdepth(sepf, bst, root, height):
	if root is None:
		return 0
	elif not root:
		return 1
	else:
		if root.left is None:
			minimumdepth(root.right) + 1
		if root.

		return min(minumin(root.left), minimum(root.right)) + 1





def lca(root, result):
	if root is None:
		return 0
	elif result < root.data:
		lcs(root.left, result)
	elif result > root.data:
		lcs(root, reault)
	else:
		return root.data

time complexity: O(N)
space complexity: O(N)
def lca(root):
	while root:
		if root.data > n1 and root.data > n2:
			root = root.left
		if root.data < n1 and root.data < n2:
			root= root.right
		else:
			break
	if root in None:
		return None
	if root:
		root.data

		data = tree2.data
		root = tree1

		def transversametime(tree1, tree2):
			if not tree1 or not tree2:
				return False
			if not tree1 and not tree2:
				return True
			return tree1.data == tree2.data and transversametime(tree1.left, tree2.left) and transversametime(
				tree1.right, tree2.right)

		def transver(tree1, tree2):
			if tree1.data == tree2.data:
				return tree1
			if not tree1:
				return True
			if not tree2:
				return False
			else:
				transver(tree1.left, tree2)
				transfer(tree1.right, tree2)

		def reverseString(string):
			special_char = '[@_!#$%^&*()<>?/\|}{~:]'
			left, right = 0, len(string) - 1
			while left < right:
				if string[left] is in special_char:
					left += 1
				if string[right] is in special_char:
					right -= 1
				string[left], string[right]. = string[right], string[left]
			return string

		def reverse(string):
			stack = []
			n = 0
			while n < len(string):
				stack.append(string[n])
				string.pop()
				n += 1
			while stack:
				string.append(stack.pop())
			return string

		123.4
		423.1
		4321
		12345
		52341
		54321
		123456
		623451
		653421
		654321


		left and right
		pointer
		left, right = 0, len(string) - 1

		def triplet(arr, target):
			if len(arr) <= 2:
				return None
			if len(arr) == 3 and sum(arr) == target:
				return arr
			else:
				arr.sort()
				for i in range(len(arr) - 1):
					for j in range(i + 1, len(arr)):
						sum_of_two = arr[i] + arr[j]
						remaining = target - sum_of_two
						index = k + 1
						while arr[k] < remaining:
							result.append(arr[i], arr[j], arr[k])


edge
cases: duplicate, all
the
same
number, negative
number
okay?

def maxSubArray(nums):
	currmax, final_max = nums[0], [nums0]
	for i in range(1, len(nums)):
		currmax = max(currmax, currmax + nums[i], num[i])
		final_max = max(final_max, currmax)
	return final_max


def twosum(self, nums):
	nums.sort()
	left, right = 0, len(nums)
	temp_sum = 0
	while left < right:
		if nums[left] + nums[right] > target:
			right -= 1
		if nums[left] + nums[right] < target:
			left += 1
		else:
			return [left, right]
	return -1


def threesum(self, nums):
	result = []
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			total_two_sum = nums[i] + nums[j]
			total_two_sum *= -1
			if total_two_sum in nums:
				result.append([nums[i], nums[j], total_two_sum])

"""
Input: arr = [2,1,4,7,3,2,5]
                        ^.      ^
run one pointer untilarr[i] < arr[i+1]  => mountain => create two pointers 
1. one mountain 
distance = 0
base is i 
peak = False
keep claming => if arr[i+1] > arr[i] => distance += 1 
reach the peak => if arr[i+1] <= arr[i]=> distance += 1 => claim down => peak == True 
reach the bottom => if arr[i+1] >= arr[i] => finaldistance = max(distance, finaldisance), peak = False 
2. another mountain inside it
if peak is True:
	if arr[i+1] > arr[i] => base = i, distance = 1
	

if arr[i] < arr[i+1] => mountain
left, right
if arr[left] < arr[left+1] => yes
if arr[right] < arr[right-1] => yes
if arr[right] > arr[right-1] => continue increaing right to check the length of the mountain 


egde case: array length less than 3 => return False, all array same length => Return False => 
technique use: use two pointer to keep track of when we see the mountain, there could be another mountain after the valley, we keep the distance of the previous one, and check which ever mountain is higher
variable use: two pointer,
data structure: for loop, no new array created
time complexity: O(N)
space complexity: O(1)

def sol(arr):
	if len(arr) < 3:
		return False	
		
		
Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

#minheap
find parent index =  len(arr)//2, 
if parent > value:
	swap(parent, value)
recuesive calling the function again passing (arr, currIndex, value):
base case: when parent < value: return 
def heapify(self, arr, currIndex(the length of the array because we adding value to the end), value):
	
	
		
"""


def bst(arrs, left, right, finalarea):
	if left == right:
		return finalarea
	else:
		minvalue = min(arrs)
		midindex = max(arrs.indexof(minvalue))
		maxarea = minvalue * (right - left + 1)
		finalarea = max(maxarea, finalarea)

		self.bst(arrs, left, midindex - 1, finalarea)
		self.bst(arrs, midindex + 1, right, finalarea)
	return max(finalarea, maxarea)


def findarea(arrs):
	# edge cases:
	if len(arrs) <= 1:
		return -1
	left, right = 0, len(arrs)
	finalarea = 0
	self.bst(arrs, left, right, finalarea)

"""
word: abc  char => value 
	  012  index  => key
""""
def permutation_using_hashmap(word, text):
	hm = {}
	for i in range(len(word)):
		hm[word[i]] = i
	left, right = 0, len(word)
	while right <= len(text):

		def permutation(self, word, text):
			if len(word) == 1 and word in text:
				return word
			else:
				word.sort()
				left, right = 0, len(word)
				while right <= len(text):
					window = text[left:right]
					window_clone = window
					window.sort()
					if window is in word:
						result.append(window_clone)
					left += 1
					right += 1

"""
use stack, recursive 
base case: visited all node, reach the end

"""
def depth_first_search(dictionary, boggle):
	row = len(boggle)
	column = len(boggle[0])
	result = []
	dicindex= 0
	for c in range(column):
		for r in range(row):
			for index in range(len(dictionary)):
				if boggle[c][r] in dictionary[index]:
					dfs(boggle, c, r, dictionary[index], dicindex, result)

def dfs(boggle, c, r, dictionary, dicindex , result):
	if c < 0 or r < 0 or c > len(boggle[0]) or r > len(boggle) or boggle[c][r].isVisited():
		return
	if dicindex == len(dictionary):
		result.append(dictionary)
	else:
		return dfs(boggle,c+1, r, dictionary, dicindex+1, result)
		return dfs(boggle,c-1, r, dictionary, dicindex+1, result)
		return dfs(boggle,c, r+1, dictionary, dicindex+1, result)
		return dfs(boggle,c, r-1, dictionary, dicindex+1, result)



#Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
"""
technique: 
data structure:
time:
space: 
"""
def lcp(str):
	if len(str) <= 1:
		return str
	else:
		result = ""
		temp =""
		for i in range(len(str)-1):
			if len(temp) != len(result):
				result = temp
			for j in range(len(str[i])):
				while str[i][j] ==str[i+1][j]:
					temp += str[i][j]
"""
technique: divie and conqert, recurisve
time: O(2^N)
space: O(1)
base case: when string break down to only two variables
variable needed: index of left, right, and mid


"""
def lcp_divide_and_conquert(str, left, right):
	#divide step
	if left < right:
		mid = (left + (right-left))//2
		lcp_divide_and_conquert(str, left, mid-1)
		lcp_divide_and_conquert(str, mid+1, right)
	return conquer(str, left, right)


def conquer(str, left, right):
	str[left].sort()
	str[right].sort()
	index = 0
	result = ""
	while str[left][index] == str[right][index]:
		result += str[left][index]
	return result


def quicksort(arr):
	pivot = len(arr) -1


def hollow_pyramid_triangle_pattern(N):
	for i in range(N):
		for j in range(N):
			if i == 0 and j == N/2:
				print("#", end = "")
			print(" ", end = "")
			if i == N:
				print("#", end = "")

def array_rotation(arr, d):
	n = len(arr)
	#use temp array
	temp_arr = [0 ] * n
	while d < n:
		temp_arr[d].append(arr[d])
		d+= 1
	index = 0
	for i in range(d, n):
		temp_arr[d] = arr[index]
		index += 1

def is_palindrome(str):
	if len(str) == 1:
		return True
	else:
		left, right = 0, len(str)-1
		while left < right:
			if str[left] != str[right]:
				return False
			left += 1
			right -= 1
		return True
def longest_palindrome(arrlist):
	maxlength = 0
	for arr in arrlist:
		if is_palindrome(arr):
			maxlength = max(maxlength, len(arr))
	return maxlength

def decimal_to_binary(decimal):

	quotient = decimal
	remainder = 0
	binary = 0
	while quotient > 1:
		quotient = decimal / 2
		remainder = decimal % 2
		if remainder == 1:
			binary += 1
			binary *= 10
		decimal /= 2

def gcd(num1, num2):
	gcd_list = []
	if num2 < num1:
		num1, num2 = num2, num1
	for i in range(1,num1+1):
		if num1 % i == 0 and num2 % i == 0:
			gcd_list.append(i)
	return gcd_list

"""
0011001

"""
def binary_to_decimal(binary):
	if binary == 0:
		return -1
	else:
		binary = str(binary)
		decimal = 0
		index = len(binary)-1
		power = 1
		while index >= 0:
			if binary[index] == 1:
				decimal += power
			power *= 2
			index -= 1


class ValidExpression:
	# Checks if the given expression is valid
	def isExprValid(self, expr):
		number = eval(expr)
		print(number)

		"""
        We traverse the string from left to right and maintain 2 stacks
         – one for numbers and the other one for operators and 
         parentheses.
          When we encounter a number we push it to the 
         integer stack and similarly, in case of an operator or an
        open bracket, we push it to the character stack. 

        When we encounter a closed bracket, we remove characters from 
        the character stack until we encounter the corresponding 
        open parentheses. Also, when we get an operator we remove 
        2 integers from the integer stack. In case we are not able
        to perform any of the operations, we return false, thus 
        considering the expression invalid. 
        """


"""        stack_number, stack_operate_parenttheless = [], []
        operator = ["+", "-", "*"]
        for i in range(len(expr)-2):
            if expr[i] is " ":
                continue
            while expr[i].isdigit():
                stack_number.append(expr[i])
                i += 1
            if expr[i] is operator or expr[i] == "(":
                stack_operate_parenttheless.append(expr[i])
            if expr[i] == ")":
                for char in stack_operate_parenttheless:
                    if char == "(":
                        break
                    if char is operator:
                        stack_number.pop()
                        stack_number.pop()
                    stack_operate_parenttheless.pop()
            else:
                return False
        if len(stack_number) != 0 and len(stack_operate_parenttheless)!= 0:
            return False
        return True"""


def main():
	# Take Input
	expr = input()

	# Print result
	result = "yes" if ValidExpression().isExprValid(expr) else "no"
	print(f"{result}: {expr}")


# Call the main method
main()












