class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 特殊情况处理，输入的字符串列表为空，直接给返回空字符串“”
        if not strs:
            return ""
        # 确定比较长度，找到输入字符串列表中最短字符串的长度，
        # 将其作为后续比较的最大长度范围。
        #生成器表达式，内置函数min
        min_len = min(len(s) for s in strs)
        # 字符比较循环{外层：从0到最短字符长度}
        for i in range(min_len):
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] !=c:
                    return strs[0][:i]
        return strs[0][:min_len]
