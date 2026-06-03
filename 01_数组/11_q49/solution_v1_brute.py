from typing import List

def groupAnagrams_v1(strs: List[str]) -> List[List[str]]:
    """
    方法一：暴力匹配
    思路：维护一个结果列表，每遇到一个新单词，就去结果列表中寻找是否有匹配的组。
    """
    res = []
    
    # 辅助函数：判断两个字符串是否是字母异位词
    def isAnagram(s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        # 排序后对比是最简单的暴力检查方法
        return sorted(s1) == sorted(s2)

    for s in strs:
        found = False
        # 遍历当前已经分好的组
        for group in res:
            # 只需要和组内的第一个元素对比即可
            if isAnagram(s, group[0]):
                group.append(s)
                found = True
                break
        # 如果没找到匹配的组，新建一组
        if not found:
            res.append([s])
            
    return res

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"]
    ]
    for tc in test_cases:
        print(f"输入: {tc}")
        print(f"输出: {groupAnagrams_v1(tc)}")
        print("-" * 20)
