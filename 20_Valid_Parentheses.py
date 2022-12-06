class Solution:
    def isValid(self, s: str) -> bool:
        dic = { '}':  '{'  , ']' : '[' , ')' : '('}
        stack = []
        for i in s:
            if not stack and (i == ")" or i == "]" or i == "}"):
                return False
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if stack.pop() == dic.get(i):
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
class __main__():
    instance = Solution()
    print(instance.isValid("["))
