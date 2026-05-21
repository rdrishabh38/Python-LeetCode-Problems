# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lowercase English letters if it is non-empty.

import sys
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    solution = Solution()
    
    try:
        # 1. Read the number of test cases
        t = int(input().strip())
        
        for _ in range(t):
            # 2. Read N (the size of the array). 
            # Note: We read it, but we don't actually need to use 'n' in Python 
            # since .split() automatically handles the array sizing for us!
            n = int(input().strip())
            
            # 3. Read the line of strings and split them by spaces into a List[str]
            # Example: "flower flow flight" becomes ["flower", "flow", "flight"]
            strs = input().strip().split()
            
            # 4. Execute your logic
            ans = solution.longestCommonPrefix(strs)
            
            # 5. Print the output exactly as expected. 
            # If the answer is an empty string "", it will just print a blank line, 
            # which is what HackerEarth expects.
            print(ans)
            
    except EOFError:
        # This catches edge cases where HackerEarth has malformed hidden test files
        # with trailing blank lines at the very end of the document.
        pass