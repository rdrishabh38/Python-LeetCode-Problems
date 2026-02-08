# Problem 2: Valid Palindrome
# The Problem: Given a string s, return true if it is a palindrome, or false otherwise.

# The Crucial Rule: For this problem, you must first convert the string to lowercase and remove all non-alphanumeric characters (punctuation, spaces, symbols, etc.). The palindrome check is performed on this "cleaned" string.

# (An alphanumeric character is a letter or a number).

# Examples:

# Input: s = "A man, a plan, a canal: Panama"

# Output: True

# Explanation: After cleaning, the string becomes "amanaplanacanalpanama", which is a palindrome.

# Input: s = "race a car"

# Output: False

# Explanation: After cleaning, the string becomes "raceacar", which is not a palindrome.

# Input: s = " "

# Output: True

# Explanation: After cleaning, the string becomes "" (an empty string). An empty string reads the same forward and backward, so it is a palindrome.


class palindrome:

    def ispalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        counter_front = 0
        counter_back = len(cleaned_s) - 1
        for i in range(len(cleaned_s) // 2):
            if cleaned_s[counter_front] == cleaned_s[counter_back]:
                counter_front += 1
                counter_back -= 1
            else:
                return False
        return True
    

if __name__ == "__main__":
    solution = palindrome()
    print(solution.ispalindrome("A man, a plan, a canal: Panama"))  # True
    print(solution.ispalindrome("race a car"))  # False
    print(solution.ispalindrome(" "))  # True

