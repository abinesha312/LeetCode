class Solution:
    '''
        Diffculty leve : Easy
        Using the Hasmap finding the duplicate in the string
    '''
    def DUplicateCheck(self,nums:list[int])->list[int]:
        HasMap = {}
        for i,n in enumerate(nums):
            if n in HasMap:
                return True
            else:
                HasMap[n] = i
        return False



if __name__ == '__main__':
    cCall = Solution()
    nums = [1,2,3,4,5,1]
    val = cCall.DUplicateCheck(nums)
    print(val)
