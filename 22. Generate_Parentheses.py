class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(curr='', open_count=0, close_count=0):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if open_count < n:
                backtrack(curr + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ')', open_count, close_count + 1)

        backtrack()
        return res
