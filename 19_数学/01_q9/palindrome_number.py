class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也必须是 0，只有 0 满足这一属性。
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10

        # 当数字长度为奇数时，我们可以通过 revertedNumber // 10 去除处于中位的数字。
        # 例如，当输入为 121 时，在 while 循环的末尾我们可以得到 x = 1，revertedNumber = 12，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        return x == revertedNumber or x == revertedNumber // 10

    def isPalindromeWithLogs(self, x: int) -> bool:
        print(f"\n[开始检测] 整数: {x}")
        
        if x < 0 or (x % 10 == 0 and x != 0):
            print(f"-> 快速判定: {'负数' if x < 0 else '以 0 结尾'}，一定不是回文。")
            return False

        revertedNumber = 0
        original_x = x
        step = 0
        
        print(f"初始状态: x = {x}, revertedNumber = {revertedNumber}")
        
        while x > revertedNumber:
            step += 1
            last_digit = x % 10
            revertedNumber = revertedNumber * 10 + last_digit
            x //= 10
            print(f"步骤 {step}: x 剩余 = {x: <5} | revertedNumber = {revertedNumber: <5} (取出的位: {last_digit})")

        # 结果判断
        is_even_match = (x == revertedNumber)
        is_odd_match = (x == revertedNumber // 10)
        result = is_even_match or is_odd_match
        
        print(f"最终对比: x({x}) == reverted({revertedNumber}) [偶数位匹配: {is_even_match}]")
        print(f"最终对比: x({x}) == reverted({revertedNumber//10}) [奇数位匹配: {is_odd_match}]")
        print(f"结论: {original_x} {'是' if result else '不是'}回文数。\n")
        return result

if __name__ == "__main__":
    solution = Solution()
    
    # 使用带日志的方法演示几个典型案例
    demo_cases = [1221, 12321, 123, 10, -121]
    for case in demo_cases:
        solution.isPalindromeWithLogs(case)
