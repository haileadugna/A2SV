class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        numbertasks = Counter(tasks)
        settasks = list(set(tasks))
        res = 0
        for task in settasks:
            if numbertasks[task] == 1:
                return -1
            elif numbertasks[task]%3 >=1:
                res += numbertasks[task]//3 + 1
            else:
                res += numbertasks[task]//3
        return res