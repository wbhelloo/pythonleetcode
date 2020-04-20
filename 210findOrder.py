from collections import defaultdict
from collections import deque


class Solution(object):

    # 正向建立图，当nxt节点的入度变为0，代表这个节点可以加入res
    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        du = [0] * numCourses
        requisites = defaultdict(list)
        for cur, pre in prerequisites:
            du[cur] += 1
            requisites[pre].append(cur)

        # 校验是否成环 如果是没环
        if len(requisites.keys()) > numCourses - 1:
            return []
        course = []
        for key, item in enumerate(du):
            if item == 0:
                course.append(key)

        if len(course) == 0:
            return []

        nodelist = deque(course)
        out = []
        while nodelist:
            node = nodelist.popleft()
            out.append(node)
            for item in requisites[node]:
                du[item] -= 1
                if not du[item]:
                    nodelist.append(item)
        if any(item for item in du):
            return []
        return out

    # 反向思维，出度为0的为最后一个点，反推
    def findOrder(self, numCourses, prerequisites):
        requisites = defaultdict(list)
        out = [0 for _ in range(numCourses)]

        for nxt, pre in prerequisites:
            requisites[nxt].append(pre)
            out[pre] += 1
        stk = []
        for key, item in enumerate(out):
            if item == 0:
                stk.append(key)

        if len(stk) == 0:
            return []

        stack = []

        while stk:
            node = stk.pop()
            stack.append(node)
            for pre in requisites[node]:
                out[pre] -= 1
                if out[pre] == 0:
                    stk.append(pre)

        if len(stack) < numCourses:
            return []

        return list(reversed(stack))


if __name__ == '__main__':
    sol = Solution()
    n = 4
    course = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(sol.findOrder(n, course))
