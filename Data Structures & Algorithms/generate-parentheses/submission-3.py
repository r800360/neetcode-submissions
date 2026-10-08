class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        join = ["()"]

        def backtrack(curr, num):
            two_num = 2 * num
            if len(curr) > two_num:
                return
            if len(curr) == two_num:
                result.add(curr)
                return

            # 0 <= len(curr) < 2*n; curr % 2 == 0
            left_curr = "(" + curr
            for i in range(1, two_num):
                new_curr = left_curr[:i] + ")" + left_curr[i:]
                backtrack(new_curr, num)

        # backtrack takes n -> n+1 using result to eliminate duplicates and join to hold the result
        for i in range(2, n+1):
            join_len = len(join)
            while join_len > 0:
                curr = join.pop(0)
                backtrack(curr, i)
                join += list(result)
                result.clear()
                join_len -= 1

        return list(set(join))