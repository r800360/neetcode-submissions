class Solution:
    def add(self, num1: str, num2: str) -> str:
        result = ""
        i = 0
        carry_value = 0
        n1 = len(num1)
        n2 = len(num2)
        while i < n1 or i < n2:
            num1_digit = ord(num1[-1-i]) - ord("0") if i < n1 else 0
            num2_digit = ord(num2[-1-i]) - ord("0") if i < n2 else 0
            single_result = num1_digit + num2_digit + carry_value
            sum_value = single_result % 10
            carry_value = single_result // 10
            result = f"{sum_value}{result}"
            i += 1
        
        if carry_value:
            result = f"{carry_value}{result}"
            
        return result


    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        result = ""
        n1 = len(num1)
        n2 = len(num2)
        
        for i in range(n2):
            num2_digit = ord(num2[-1-i]) - ord("0")
            carry_value = 0
            single_multiply = ""
            for j in range(n1):
                num1_digit = ord(num1[-1-j]) - ord("0")
                single_result = num1_digit * num2_digit + carry_value
                sum_value = single_result % 10
                carry_value = single_result // 10
                single_multiply = f"{sum_value}{single_multiply}"
            if carry_value > 0:
                single_multiply = f"{carry_value}{single_multiply}"
            single_multiply += "0" * i
            if not result:
                result = single_multiply
                continue
            # Add result and singleMultiply
            result = self.add(result, single_multiply)

        return result