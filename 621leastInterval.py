from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        if not tasks:
            return 0
        dict_task = dict()
        for task in tasks:
            dict_task[task] = dict_task.get(task, 0) + 1

        dict_task = sorted(dict_task.items(), key=lambda x: x[1], reverse=True)

        res = (n + 1) * (dict_task[0][1] - 1)

        for k, n in dict_task:
            if n == dict_task[0][1]:
                res += 1

        return res if res > len(tasks) else len(tasks)


if __name__ == '__main__':
    sol = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2

    print(sol.leastInterval(tasks, n))
