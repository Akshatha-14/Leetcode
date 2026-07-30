class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        bracket={"]":"[",")":"(","}":"{"}
        for ch in s:
            if ch in bracket:
                if stack and stack[-1]==bracket[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False