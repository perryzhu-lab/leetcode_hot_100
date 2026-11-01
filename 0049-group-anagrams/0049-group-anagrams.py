from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 创建空字典
        hash_map=defaultdict(list)
        # 遍历输入数组里的每一个字符串s
        for s in strs:
            # 把s排序，得到key
            sorted_chars=sorted(s)
            key=''.join(sorted_chars)
            # 原始字符串s加入到字典对应key的列表
            hash_map[key].append(s)
        return list(hash_map.values())