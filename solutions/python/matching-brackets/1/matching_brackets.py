def is_paired(input_string):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for c in input_string:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1] != bracket_map[c]:
                return False
            stack.pop()
    
    return not stack
