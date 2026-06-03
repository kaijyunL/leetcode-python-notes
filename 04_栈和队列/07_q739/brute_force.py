from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    暴力解法：双重循环
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    n = len(temperatures)
    ans = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break
    return ans

if __name__ == "__main__":
    test_data = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"输入: {test_data}")
    print(f"输出: {dailyTemperatures(test_data)}")
