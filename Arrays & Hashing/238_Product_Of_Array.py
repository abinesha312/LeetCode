class Solution:
    '''
        Diffculty leve : Medium
        - first we calculate the multiplication of prefix values and store them in the response
        - Second we multiple the res * into the nums in the reverse order of the given array where with the post fix value 
    '''
    def ProductArray(self,nums:list[int])->list[int]:
        res = [1]*len(nums)
        pre=1
        for i in range(len(nums)):
            res[i]*=pre
            pre*=nums[i]
        post=1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post*=nums[i]
        return res




if __name__ =='__main__':
    cc= Solution()
    nums = [1,2,3,4]
    res = cc.ProductArray(nums)
    print(res)