
# checks if a word/phrase is a palindrome(its the same if reversed)

def palindrome(s):
    s = s.replace(' ', '')
    print(s[::-1] == s)


palindrome('nurses run')
