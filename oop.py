class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = 0
        """
        [0 , 1 , 0 , 3 , 12]
         ^   ^
         [1, 0, 0, 3, 12]
             ^     ^
        [1, 3, 0, 0, 12]
               ^.     ^ 
        """
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1
        return nums
            
                
                
        