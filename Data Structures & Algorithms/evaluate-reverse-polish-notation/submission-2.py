class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        i = 0

        while i < len(tokens):
            #digit 
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            #operation
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+' :
                    stack.append(a+b)
                elif tokens[i] == '-':
                    stack.append(b-a)
                elif tokens[i] == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
            i += 1 

        return stack[-1]

