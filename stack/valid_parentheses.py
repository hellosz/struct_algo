# 有效括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution:
    def isValid(self, s: str) -> bool:
        # 匹配符号映射字典
        valid_dic = {'}': '{', ']': '[', ')': '('}
        # 用栈来验证是否匹配
        stack = []
        for symbol in s:
            if symbol in valid_dic:
                if not stack or stack.pop() != valid_dic[symbol]:
                    return False
            else:
                stack.append(symbol)
        return len(stack) == 0
solution = Solution()
print(solution.isValid('()[]{}'))