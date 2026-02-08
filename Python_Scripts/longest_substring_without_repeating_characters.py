# 🧩 Problem 4: Longest Substring Without Repeating Characters
# The Problem: Given a string s, find the length of the longest substring that 
# does not contain any repeating characters.

# Definitions:

# Substring: A contiguous (unbroken) sequence of characters within a string. 
# "wke" is a substring of "pwwkew", but "pwke" is not.

# Examples:

# Input: s = "abcabcbb"

# Output: 3

# Explanation: The longest substring without repeating characters is "abc", with a length of 3.

# Input: s = "bbbbb"

# Output: 1

# Explanation: The longest substring is "b", with a length of 1.

# Input: s = "pwwkew"

# Output: 3

# Explanation: The longest substring is "wke", with a length of 3. 
# Notice that "pwke" is a subsequence (not contiguous) and therefore doesn't count.


class longest_substring:

    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        right_pointer = 1
        max_length = 1
        while right_pointer <= len(s):
            if len(s[left_pointer: right_pointer]) == len(set(s[left_pointer: right_pointer])):
                current_length = right_pointer - left_pointer
                if current_length > max_length:
                    max_length = current_length
                right_pointer += 1
            else:
                left_pointer += 1
        if len(s) == 0:
            return 0
        return max_length


class longest_substring_sliding_window:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # A set to store the characters currently in our window
        chars_in_window = set()
        
        max_length = 0
        left = 0
        
        # The 'right' pointer will be our main loop
        # It expands the window
        for right in range(len(s)):
            
            # This is the "shrink" logic.
            # If the new character s[right] is ALREADY in our set,
            # we have a duplicate. We must shrink the window from the left
            # until the *old* duplicate is removed.
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1
            
            # Now that we're sure there are no duplicates,
            # add the new character s[right] to our window set.
            chars_in_window.add(s[right])
            
            # Update the max_length.
            # The current valid window length is (right - left + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length

    

if __name__ == "__main__":
    test = longest_substring()
    print(test.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(test.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(test.lengthOfLongestSubstring("pwwkew"))    # Output: 3


    test = longest_substring_sliding_window()
    print(f"'abcabcbb': {test.lengthOfLongestSubstring('abcabcbb')}")
    print(f"'bbbbb': {test.lengthOfLongestSubstring('bbbbb')}")
    print(f"'pwwkew': {test.lengthOfLongestSubstring('pwwkew')}")
    print(f"'': {test.lengthOfLongestSubstring('')}") # Handles empty string