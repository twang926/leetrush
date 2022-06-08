import functools
from nis import match
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        target = total // 4
        
        matchsticks = tuple(sorted(matchsticks, reverse=True))
        if total % 4 != 0:
            return False
        
        @functools.lru_cache(None)
        def dfs(lst, cur):
            if cur == target:
                if sum(lst) == target:
                    return True
                if sum(lst) < 2 * target:
                    return False
                return dfs(lst[1:], lst[0])
            elif cur > target:
                return False
            else:
                for i in range(len(lst)):
                    if cur + lst[i] <= target:
                        if dfs(lst[:i] + lst[i+1:], cur + lst[i]):
                            return True
                return False

        return dfs(tuple(matchsticks), 0)


if __name__ == '__main__':
    print( Solution().makesquare([4,1,3,1, 3, 5]))
    

