class Solution:
    def isValid(self, s: str) -> bool:
        """
        hashm={}

        """
        mapping={")":"(", "}":"{" , "]":"[" }
        stack=[]
        for par in s:
            if par in mapping:
                if stack and stack[-1]==mapping[par]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(par)

        return True if not stack else False

        































        # stack=[]
        # opening=["(","[","{"]
        # for i in s:
        #     if i in opening:
        #         stack.push(i)
        #     else:
        #         if stack is not None and stack.pop()==i:

        