def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    opcl = dict(('{}', '[]', '()'))
    stack = []

    for i in s:
        if i in '({[':
            stack.append(i)
        elif len(stack) == 0 or i != opcl[stack.pop()]:
            return False

    return len(stack) == 0


print(isValid("()[]{}"))
