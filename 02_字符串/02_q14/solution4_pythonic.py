from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        解法四：Pythonic 魔法解法 (zip + set)
        思路：使用 zip(*strs) 按列解包，用 set 检查每一列是否完全相同。
        """
        if not strs:
            return ""
        
        res = ""
        # zip(*strs) 会在最短的字符串耗尽时自动停止
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                res += chars[0]
            else:
                break
                
        return res

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
        (["apple", "ape", "april"], "ap"),
        (["a"], "a"),
        ([], "")
    ]
    
    print("--- 正在运行 解法四 (Pythonic zip+set) ---")
    for strs, expected in test_cases:
        result = sol.longestCommonPrefix(strs)
        print(f"输入: {strs}, 期望: '{expected}', 结果: '{result}' - {'成功' if result == expected else '失败'}")
