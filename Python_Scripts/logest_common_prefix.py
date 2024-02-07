"""Question: Write a function to find the longest common prefix string amongst an array of strings.
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'."""

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res=''
    flag=0
    for i in range(len(strs[0])):
        for element in strs:
            if i<len(element) and strs[0][i]==element[i]:
                flag=0
            else:
                flag=1
                return res
                
        if flag==0:       
            res+=strs[0][i]
    return res

