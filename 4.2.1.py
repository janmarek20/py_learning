def is_palindrome(word):
    """
    The function returns True if the given word (argument) is a palindrome
    Argument:
    word (string type)
    """
    if word == word[::-1]:
        return True
    else:
        return False
    

print(is_palindrome("kajak"))
print(is_palindrome("burza"))