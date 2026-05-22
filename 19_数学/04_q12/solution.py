class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义所有基础值和特殊情况的映射关系
        # 我们按照从大到小的顺序排列，以实现“贪心”策略
        val_to_sym = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        res = []
        
        # 遍历我们的映射表
        for value, symbol in val_to_sym:
            # 如果 num 为 0，说明已经处理完毕，可以直接退出了
            if num == 0:
                break
            
            # 使用 divmod 可以同时得到 商（需要重复多少次这个符号）和 余数（剩下的数）
            count, num = divmod(num, value)
            
            # 把符号重复 count 次，拼接到结果中
            res.append(symbol * count)
        
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    # 测试一些典型的例子
    print(f"3 -> {sol.intToRoman(3)}")      # 期望: III
    print(f"58 -> {sol.intToRoman(58)}")    # 期望: LVIII (50 + 5 + 3)
    print(f"1994 -> {sol.intToRoman(1994)}")# 期望: MCMXCIV (1000 + 900 + 90 + 4)
