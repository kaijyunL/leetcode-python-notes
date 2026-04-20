from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        for _ in range(2, n + 1):
            # 使用列表收集片段，最后 join，避免字符串 += 反复创建新对象
            parts = []
            
            # groupby 将连续重复的元素分组，返回值是由 (当前连续字符, 包含前面连续字符可迭代对象) 组成的迭代器
            # 比如 "111221" 遍历时先后产出：('1', 迭代器元素['1','1','1']), ('2', ['2','2']), ('1', ['1'])
            for digit, group in groupby(res):
                # 用生成器计数，避免 len(list(group)) 产生临时列表
                count = sum(1 for _ in group)
                parts.append(str(count) + digit)
                
            res = ''.join(parts)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print("解法三：Pythonic 优雅解法 (itertools.groupby)")
    print("第 1 项:", solution.countAndSay(1))
    print("第 4 项:", solution.countAndSay(4))
    print("第 5 项:", solution.countAndSay(5))
