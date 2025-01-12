class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2!=0:
            return False
        
        open_brackets, unlocked = 0,0
        for i in range(n):
            if locked[i] == "0":
                unlocked+=1
            elif s[i]=="(":
                open_brackets+=1
            elif s[i]==")":
                if open_brackets>0:
                    open_brackets-=1
                elif unlocked>0:
                    unlocked-=1
                else:
                    return False
        
        balance_count = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == "0":
                balance_count -= 1
                unlocked -= 1
            elif s[i] == "(":
                balance_count += 1
                open_brackets -= 1
            elif s[i] == ")":
                balance_count -= 1
            if balance_count > 0:
                return False
            if unlocked == 0 and open_brackets == 0:
                break

        if open_brackets > 0:
            return False

        return True