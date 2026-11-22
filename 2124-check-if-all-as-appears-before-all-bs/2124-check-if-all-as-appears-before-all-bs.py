class Solution:
    def checkString(self, s: str) -> bool:
        found_b = False

        for i in s:
            if i == 'b':
                found_b = True
            elif found_b and i == 'a':
                return False

        return True