#Runtime - 103 ms	
#Memory - 14.1 MB
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] != val:
                i = i + 1
            else:
                nums.pop(i)
