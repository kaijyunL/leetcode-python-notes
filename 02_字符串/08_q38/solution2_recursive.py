class Solution:
    def countAndSay(self, n: int) -> str:
        # 1. 递归的终止条件，第一项必定是 "1"
        # 注意：题目约束 1 ≤ n ≤ 30，递归深度不会溢出
        if n == 1:
            return "1"
        
        # 2. 递推：先获取上一项 n-1 的结果
        prev = self.countAndSay(n - 1)
        
        # 使用列表收集片段，最后 join，避免字符串 += 反复创建新对象
        parts = []
        i = 0
        
        # 3. 对上一项的字符串进行 "计数和描述" 的操作
        while i < len(prev):
            count = 1
            
            # 统计连续相同字符的出现次数
            while i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
                i += 1
                
            # 拼接描述：几个几，比如 3 个 1 就是 "31"
            parts.append(str(count) + prev[i])
            i += 1
            
        # 返回当前层的结果给上一层
        return ''.join(parts)

if __name__ == "__main__":
    solution = Solution()
    print("解法二：递归解法")
    print("第 1 项:", solution.countAndSay(1))
    print("第 4 项:", solution.countAndSay(4))
    print("第 5 项:", solution.countAndSay(5))
