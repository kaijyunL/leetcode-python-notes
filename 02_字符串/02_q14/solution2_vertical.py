from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        解法二：纵向扫描
        思路：比较所有字符串在同一列（索引）上的字符是否相同
        """
        if not strs:
            return ""
        
        # 遍历第一个字符串的每一个字符
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # 检查其他所有字符串在第 i 个位置的字符
            for j in range(1, len(strs)):
                # 两个退出条件：
                # 1. 当前索引 i 已经超过了某个字符串的长度
                # 2. 当前字符与第一个字符串的字符不一致
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["apple", "ape", "april"], "ap")
    ]
    
    for strs, expected in test_cases:
        result = sol.longestCommonPrefix(strs)
        print(f"输入: {strs}, 期望: '{expected}', 结果: '{result}' - {'成功' if result == expected else '失败'}")
