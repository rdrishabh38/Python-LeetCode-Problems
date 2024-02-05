# Question Link : https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        """

        :s: input string of roman numerals
        """

        # creating a dict of fundamental elements in Roman Numerology

        dict_roman_fundamental_elements = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                                           'C': 100, 'D': 500, 'M': 1000}

        # Dict of known cases as per question description

        # Roman numerals are usually written largest to smallest from left to right.
        # However, the numeral for four is not IIII. Instead, the number four is written
        # as IV. Because the one is before the five we subtract it making four.
        # The same principle applies to the number nine, which is written as IX.
        # There are six instances where subtraction is used:
        #
        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        dict_roman_subtraction_instances = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                                            'CD': 400, 'CM': 900}

        if s in dict_roman_subtraction_instances.keys():
            return dict_roman_subtraction_instances[s]
        output = 0
        input_list_characters = []
        for character in s:
            input_list_characters.append(character)

        print(input_list_characters)
        for index, character in enumerate(input_list_characters):
            print("output is = {}".format(output))
            if (index + 1) < len(input_list_characters):
                if character == 'I' and input_list_characters[index + 1] == 'V':
                    output = output + 4
                    input_list_characters.pop(index)
                elif character == 'I' and input_list_characters[index + 1] == 'X':
                    output = output + 9
                    input_list_characters.pop(index)
                elif character == 'X' and input_list_characters[index + 1] == 'L':
                    output = output + 40
                    input_list_characters.pop(index)
                elif character == 'X' and input_list_characters[index + 1] == 'C':
                    output = output + 90
                    input_list_characters.pop(index)
                elif character == 'C' and input_list_characters[index + 1] == 'D':
                    output = output + 400
                    input_list_characters.pop(index)
                elif character == 'C' and input_list_characters[index + 1] == 'M':
                    output = output + 900
                    input_list_characters.pop(index)
                else:
                    output = output + dict_roman_fundamental_elements[character]
            else:
                output = output + dict_roman_fundamental_elements[character]
        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMXCIV"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("III"))

