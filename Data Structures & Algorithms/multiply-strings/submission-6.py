class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                prod = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                sum_idx = i + j
                # Add calculated product onto what is already there
                sum_val = prod + pos[sum_idx + 1]
                pos[sum_idx] += sum_val // 10
                pos[sum_idx+1] = sum_val % 10

        result = ""
        for val in pos:
            if (val != 0 or len(result) != 0):
                result += str(val)
        
        if len(result) == 0:
            return "0"
        
        return result