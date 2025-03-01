class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        for letter in ransomNote:
            ransom_dict[letter] = ransom_dict.get(letter, 0) + 1
        for letter in magazine:
            if letter in ransom_dict:
                ransom_dict[letter] -= 1
        for digit in ransom_dict.values():
            if digit > 0:
                return False
        return True