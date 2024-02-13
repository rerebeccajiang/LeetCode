class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(combo: str, lCnt: int, rCnt: int, n: int, res: List[str]):
            if lCnt == rCnt == n:
                res.append(combo)
            if lCnt < n:
                backtrack(combo+"(", lCnt+1, rCnt, n, res)
            if lCnt > rCnt:
                backtrack(combo+")", lCnt, rCnt+1, n, res)

        res = []
        backtrack("", 0, 0, n, res)
        return res
        