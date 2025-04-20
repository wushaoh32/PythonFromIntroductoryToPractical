class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for ch in s:
            if ch in pairs:#如果是左括号
                stack.append(ch)
            else:#如果是右括号
                if not stack or pairs[stack.pop()] != ch:
                    return False
        return not stack
#pairs使用[]是字典的兼职访问操作
#对于容器类型，如果为空则会返回False,这里的的not False表示：如果栈是空，则not stack为True,继续执行
#栈不为空时，not stack为False，不执行后续代码
#最下面的return：因为如果匹配就会弹出来，到最后栈会是空的，return not stack就是个True
solution = Solution()
test_case1 = "()[]{}"
print(f"测试用例{test_case1}的结果是{solution.isValid(test_case1)}")
#isvalid是判断输入的字符串是否是有效的括号组合