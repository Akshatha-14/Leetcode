class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i in range (len(nums)):
            ans=target-nums[i]

            if ans in seen:
                return [seen[ans],i]
            else:
                seen[nums[i]]=i