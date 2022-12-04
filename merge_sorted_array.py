#Runtime - 61 ms
#Memory -  13.9 MB
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) > 0:
            j = 0
            for i in range(len(nums1)):
                if j< len(nums2) and nums2[j] < nums1[i]:
                    nums1.insert(i,nums2[j])
                    j = j +  1
                    nums1.pop()
                if len(set(nums1[i:])) == 1 and nums1[i] == 0 and j< len(nums2):
                    nums1[i] = nums2[j]
                    j = j + 1
        
