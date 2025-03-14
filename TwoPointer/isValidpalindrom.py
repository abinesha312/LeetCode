'''

'''
class Solution:
    def ispalindrome(self, s):
        """
        s: is string of sequence
        return type: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            while l<r and not self.alphNum(s[l]):
                l+=1
            while l<r and not self.alphNum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True  


    def alphNum(self, c):
        """
        c: is a chacter
        return type: bool
        """
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    cl = Solution()
    print(cl.ispalindrome(s))
