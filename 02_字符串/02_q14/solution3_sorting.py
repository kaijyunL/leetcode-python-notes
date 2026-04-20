from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        解法三：排序比较法
        思路：排序后，公共前缀只取决于第一个和最后一个字符串
        """
        if not strs:
            return ""
        
        # 对列表进行字典序排序
        strs.sort()
        
        # 排序后的第一个和最后一个
        first = strs[0]
        last = strs[-1]
        
        i = 0
        # 比较这两个字符串，直到出现不一致或到达短字符串末尾
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]

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
