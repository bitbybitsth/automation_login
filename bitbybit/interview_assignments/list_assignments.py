l = ['(', '[', '{', '}', ']', ')']




def is_balanced(l):
    stack = []  # -> [(,[,{,
    opening_brackets = ('(', '{', '[')
    closing_brackets = (')', '}', ']')

    for i in l:
        if i in opening_brackets:
            stack.append(i)
        if i in closing_brackets:
            x = stack.pop() # x = '['
            index = closing_brackets.index(i) # 2
            if x != opening_brackets[index]:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

if is_balanced(l):
    print("paranthesis is balanced")
else:
    print("paranthesis are not balanced")


