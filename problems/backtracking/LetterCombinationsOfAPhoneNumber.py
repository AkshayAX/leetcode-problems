# 17. Letter Combinations of a Phone Number

'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''
from typings import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Handld no digits case
        if digits == "":
            return []

        def back_track(combo: list, target_len: int):

            # if combination length equals the digits length, then append the
            # result and pop the last value
            if len(digits) == target_len:
                result.append("".join(combo))
                return

            # select the next list of letters
            letters = number_map[digits[target_len]]
            for letter in letters:
                combo.append(letter)
                back_track(combo, target_len + 1)
                combo.pop()

        result = []
        number_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        back_track([], 0)
        return result

        # "234"
        # abc def ghi
        # loop1  a
        # loop2 d
        # loop3 g
        # "adg" -->target len acheived
        # pop the item/ next in current lopp/ next letter in letters
        # "adh"  -->target len acheived
        # "adi"  -->target len acheived
        # no more letter /bakck to loop2
        # loop2 e
        # loop3 g
        # "aeg" -->target len acheived
        # pop the item/ next in current lopp/ next letter in letters
        # "aeh"  -->target len acheived
        # "aei"  -->target len acheived
        # no more letter /bakck to loop2

        # loop2 f
        # loop3 g
        # "afg" -->target len acheived
        # pop the item/ next in current lopp/ next letter in letters
        # "afh"  -->target len acheived
        # "afi"  -->target len acheived
        # no more letter /bakck to loop2

        # loop2
        # no more letter /bakck to loop1
        # loop1 b
        # now all the above steps will be repeated with b
        # loop1 c
        # same like b ,now all the steps will be repeated with c

