class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        char_dict = defaultdict(int)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for char in alphabet:
            char_dict[char] = 0

        for my_str in strs:
            # my_str -> my_str_code
            my_str_code = ""
            for my_char in my_str:
                char_dict[my_char] += 1
            for count in char_dict.values():
                if count < 10:
                    count_str = "0" + str(count)
                else:
                    count_str = str(count)
                my_str_code = count_str + my_str_code
            
            #result[my_str_code] -> string
            result[my_str_code].append(my_str)
            for char in alphabet:
                char_dict[char] = 0

        return list(result.values())