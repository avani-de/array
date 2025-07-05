
# LeetCode 9 - Palindrome Number

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# Example
print(isPalindrome(121))  # Output: True
