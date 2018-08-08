class Solution(object):
    # By https://leetcode.com/vvvjjjaa/
    def groupAnagrams(self, strs):
        grouped = {}
        for s in strs:
            grouped.setdefault(''.join(sorted(s)), []).append(s)
        return list(grouped.values())
