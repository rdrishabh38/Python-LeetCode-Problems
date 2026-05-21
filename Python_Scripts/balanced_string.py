# Balanced Portfolios (Balanced Brackets)

# You are given a string representing a sequence of financial transactions and their closures, represented by different types of brackets: (), {}, and [].

# A sequence is considered "balanced" if:

# Every opening bracket has a corresponding closing bracket of the same type.

# The brackets are closed in the exact reverse order they were opened.

# Input Format:

# The first line contains an integer T, denoting the number of test cases.

# The next T lines each contain a single string S consisting only of the characters (, ), {, }, [, and ].

# Output Format:

# For each test case, print YES on a new line if the string is balanced. Otherwise, print NO.

# Constraints:

# 1 <= T <= 1000

# 1 <= length of S <= 1000


# Example

# Sample Input:

# 3
# {[()]}
# {[(])}
# {{[[(())]]}}


# Sample Output:
# YES
# NO
# YES



def is_balanced(s: str) -> str:
    # -----------------------------------------
    # YOUR ALGORITHMIC LOGIC GOES HERE
    # Return "YES" or "NO"
    # -----------------------------------------
    balanced_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for char in s:
        if char in balanced_dict.values():
            stack.append(char)
        elif char in balanced_dict.keys():
            if not stack or stack[-1] != balanced_dict[char]:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


if __name__ == '__main__':
    # 1. Read the number of test cases
    t = int(input().strip())
    
    # 2. Loop through each test case
    for _ in range(t):
        # Read the string for the current test case
        s = input().strip()
        
        # 3. Call your function and print the result exactly as requested
        result = is_balanced(s)
        print(result)
