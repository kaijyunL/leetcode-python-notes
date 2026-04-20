from typing import List
import collections

def groupAnagrams_v2(strs: List[str]) -> List[List[str]]:
    """
    方法二：哈希表 + 排序
    思路：字母异位词排序后必然相等。将排序后的字符串作为 Key。
    """
    # 使用 defaultdict 可以避免判断 key 是否存在的逻辑
    # key 为排序后的字符串，value 为原字符串列表
    anagram_map = collections.defaultdict(list)
    
    for s in strs:
        # 1. 对字符串进行排序，例如 "eat" -> ['a', 'e', 't']
        sorted_s = sorted(s)
        # 2. 将排序后的列表转回字符串作为字典的键 (列表不可哈希，必须转成字符串或元组)
        key = "".join(sorted_s)
        # 3. 将原字符串加入对应的组
        anagram_map[key].append(s)
        
    # 返回字典中所有的 value 即可
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
        print(f"输出: {groupAnagrams_v2(tc)}")
        print("-" * 20)
