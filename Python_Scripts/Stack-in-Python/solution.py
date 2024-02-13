class Solution:

    def isempty(self, stack):
        if len(stack) == 0:
            return 0
        else:
            return 1

    def push(self, stack, element, top):
        stack.append(element)
        top = len(stack) - 1
        return top

    def pop(self, stack, top):
        print("popped element is : {}".format(stack[top]))
        stack.pop(top)
        top = top - 1
        print("new top index is : {}".format(top))
        return top

    def top(self, stack):
        top = len(stack) - 1
        return top

    def printstack(self, stack):
        print("current stack is : {}".format(stack))


if __name__ == "__main__":
    solution = Solution()
    stack_main = []
    top_main = -1
    print("Stack is empty response = {}".format(solution.isempty(stack_main)))
    top_main = solution.push(stack_main, 1, top_main)
    top_main = solution.push(stack_main, 2, top_main)
    top_main = solution.push(stack_main, 3, top_main)
    top_main = solution.push(stack_main, 4, top_main)
    solution.printstack(stack_main)
    print("top index is {}".format(top_main))
    top_main = solution.pop(stack_main, top_main)
    top_main = solution.pop(stack_main, top_main)
    solution.printstack(stack_main)


# Output :
#
# Stack is empty response = 0
# current stack is : [1, 2, 3, 4]
# top index is 3
# popped element is : 4
# new top index is : 2
# popped element is : 3
# new top index is : 1
# current stack is : [1, 2]
