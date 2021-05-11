def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    arr = []
    for ch in parens:
        if ch == '(':
            arr.append(ch)
        elif ch == ')':
            if len(arr) == 0:
                return False
            open_p = arr.pop() 
            if open_p != '(':
                return False
    return len(arr) == 0
