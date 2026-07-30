class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        seen={}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]]=1
            else:
                seen[nums[i]]+=1
        for key,value in seen.items():
            if value>len(nums)//2:
                return key

