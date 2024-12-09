class Solution:
    def remove(self,nums:list[int],vals:int):
        r = 0
        for i in range(len(nums)):
            if nums[i] != vals:
                nums[r] = nums[i]
                r+=1
        return r 



if __name__ == '__main__':
    ClasCl = Solution().remove
    nums=[3,2,2,3]
    val=3
    res = ClasCl(nums,val)
    print(res)

