from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 本质是一个一维的，numRows如果是5，输出的符合列表就是5个，两个数相加，并把加和的数放到两个数之间
        result = []
        for i in range(numRows):  # 便利每一行，行号从0开始
            row = [1] * (i + 1)  # 初始化每一行，每一行的第一个和最后一个元素都是1，所以用1填充该行
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result