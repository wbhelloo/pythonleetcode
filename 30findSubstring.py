from typing import List
from collections import Counter


class Solution:
    # 暴力解法
    def compare(self, split_words, dict_w, per_w):
        num = len(split_words) // per_w
        dict_s = dict()
        for i in range(num):
            per_word = split_words[i * per_w:(i + 1) * per_w]
            if per_word in dict_w:
                dict_s[per_word] = dict_s.get(per_word, 0) + 1
        if dict_s == dict_w:
            return True
        return False

    def findSubstringBack(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        per_w = len(words[0])
        dict_w = Counter(words)
        len_w = len(words) * per_w
        len_s = len(s)
        right = 0
        res = []
        while right + len_w <= len_s:
            split_words = s[right:right + len_w]
            if self.compare(split_words, dict_w, per_w):
                res.append(right)
            right += 1
        return res

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        per_w = len(words[0])
        len_w = len(words)
        len_s = len(s)
        res = []
        dict_w = Counter(words)
        for i in range(per_w):
            left = i
            right = i
            dict_s = dict()
            while right + per_w <= len_s:
                split_s = s[right:right + per_w]
                if split_s in dict_w:
                    dict_s[split_s] = dict_s.get(split_s, 0) + 1
                    while dict_s[split_s] > dict_w[split_s]:
                        left_word = s[left:left + per_w]
                        dict_s[left_word] -= 1
                        left += per_w
                    if dict_s == dict_w:
                        res.append(left)
                        left_word = s[left:left + per_w]
                        dict_s[left_word] -= 1
                        left += per_w
                else:
                    left = right + per_w
                    dict_s = dict()
                right += per_w
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "aaa"
    words = ["aa","aa"]
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    print(sol.findSubstring(s, words))
