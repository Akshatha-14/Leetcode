class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=""
        for ch in s:
            if ch.isalnum():
                result+=ch.lower()
        result=list(result)
        left=0
        right=len(result)-1
        while left<right:
            if result[left]!=result[right]:
                return False
            left+=1
            right-=1
        return True
        