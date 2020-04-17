from typing import List
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        content = defaultdict(list)
        for path in paths:
            parse = path.split(' ')
            root = parse[0]
            for i in range(1, len(parse)):
                left = parse[i].find('(')
                right = parse[i].find(')')
                subpath = parse[i][:left]
                txt = parse[i][left + 1:right]
                allpath = root + '/' + subpath
                content[txt].append(allpath)
        res = []
        for key, value in content.items():
            if len(value) > 1:
                res.append(value)
        return res


if __name__ == '__main__':
    sol = Solution()
    pathstr = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    print(sol.findDuplicate(pathstr))
