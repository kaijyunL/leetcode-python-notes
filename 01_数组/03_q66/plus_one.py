from typing import List

class Solution:
    def plusOne_brute_force(self, digits: List[int]) -> List[int]:
        """
        方法一：暴力解法
        通过类型转换实现：数组 -> 字符串 -> 整数 -> 加1 -> 字符串 -> 数组
        """
        # 1. 将数组 [1, 2, 3] 转换为字符串 "123"
        num_str = "".join(map(str, digits))
        
        # 2. 将字符串转换为整数并加 1
        num = int(num_str) + 1
        
        # 3. 将结果转换回数组 [1, 2, 4]
        return [int(d) for d in str(num)]

    def plusOne_optimal(self, digits: List[int]) -> List[int]:
        """
        方法二：最优解法（进位模拟）
        从数组末尾开始遍历，处理加1和进位逻辑
        """
        n = len(digits)
        
        # 从后往前遍历
        for i in range(n - 1, -1, -1):
            # 将当前位加 1
            digits[i] += 1
            
            # 判断是否需要进位（只有加1后变成10才需要继续进位）
            if digits[i] < 10:
                # 如果没有进位，直接返回结果
                return digits
            
            # 如果产生了进位，当前位变为 0，循环继续处理上一位
            digits[i] = 0
            
        # 如果循环结束还没返回，说明是像 [9, 9, 9] 这样的情况
        # 此时 digits 变成了 [0, 0, 0]，我们需要在最前面补一个 1
        return [1] + digits

    def plusOne_while(self, digits: List[int]) -> List[int]:
        """
        方法三：While 循环解法
        手动控制索引，逻辑与 for 循环一致
        """
        i = len(digits) - 1
        
        while i >= 0:
            # 当前位加 1
            digits[i] += 1
            
            # 如果没有进位（小于10），直接返回
            if digits[i] < 10:
                return digits
            
            # 产生进位，当前位置 0，继续处理上一位
            digits[i] = 0
            i -= 1
            
        # while 结束表示最高位也进位了（如 99 -> 00）
        return [1] + digits

# --- 测试代码 ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9],
        [9, 9, 9]
    ]
    
    print("--- 开始测试 ---")
    for case in test_cases:
        print(f"\n原数组: {case}")
        
        # 测试暴力解法
        res1 = sol.plusOne_brute_force(case.copy())
        print(f"暴力解法结果: {res1}")
        
        # 测试最优解法
        res2 = sol.plusOne_optimal(case.copy())
        print(f"最优解法结果: {res2}")

        # 测试 While 解法
        res3 = sol.plusOne_while(case.copy())
        print(f"While 解法结果: {res3}")
    print("\n--- 测试完成 ---")
