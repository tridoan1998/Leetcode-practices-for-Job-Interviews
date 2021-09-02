


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







