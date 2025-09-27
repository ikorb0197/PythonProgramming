DEFAULT_TEXT = "python"

def make_palindrome(text):
    palindrome = text + text[::-1]
    return palindrome

if __name__ == "__main__":
    print(make_palindrome(DEFAULT_TEXT))
    print(make_palindrome("abc"))