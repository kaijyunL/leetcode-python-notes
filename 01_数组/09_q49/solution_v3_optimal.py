from typing import List
import collections

def groupAnagrams_v3(strs: List[str]) -> List[List[str]]:
    """
    方法三：哈希表 + 计数 (最优解)
    思路：统计每个字符串中 26 个小写字母出现的频率，以此作为哈希表的 Key。
    """
    # key 为字母频率元组，value 为原字符串列表
    anagram_map = collections.defaultdict(list)
    
    for s in strs:
        # 创建一个长度为 26 的计数数组
        counts = [0] * 26
        for char in s:
            # ord() 获取字符的 ASCII 值，减去 'a' 的 ASCII 值得到 0-25 的索引
            counts[ord(char) - ord('a')] += 1
            
        # 列表是不可哈希的（不可作为字典键），需要转换为元组 (tuple)
        key = tuple(counts)
        anagram_map[key].append(s)
        
    return list(anagram_map.values())

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"]
    ]
    for tc in test_cases:
        print(f"输入: {tc}")
        print(f"输出: {groupAnagrams_v3(tc)}")
        print("-" * 20)
