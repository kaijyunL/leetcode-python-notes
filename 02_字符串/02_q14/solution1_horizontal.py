from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        解法一：横向扫描
        思路：LCP(S1, S2, S3) = LCP(LCP(S1, S2), S3)
        """
        if not strs:
            return ""
        
        # 初始前缀设为第一个字符串
        prefix = strs[0]
        
        # 遍历数组中剩余的字符串
        for i in range(1, len(strs)):
            # 只要当前字符串不以 prefix 开头，就不断缩短 prefix
            # str.find(sub) 返回子串出现的起始索引，如果是 0 则表示以子串开头
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                # 如果前缀缩短为空，说明完全没有公共部分
                if not prefix:
                    return ""
                    
        return prefix

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
