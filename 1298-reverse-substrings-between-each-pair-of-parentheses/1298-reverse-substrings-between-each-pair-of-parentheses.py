class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack =[]
        i = 0
        while(i < len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                stackPoppedEle = []
                while(stack[-1]!='('):
                    stackPoppedEle.append(stack.pop())
                stack.pop()
                stack.extend(stackPoppedEle)
            i+=1
        return "".join(stack)

