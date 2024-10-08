class ThreePointer:
     def threeSum(self, nums: list[int]) -> list[list[int]]:
          results = []
          nums.sort()
          for i, n in enumerate(nums):
               if i > 0 and nums[i] == nums[i-1]:
                    continue
               l, r = i + 1, len(nums)-1
               while l < r :
                    diff = n + nums[l] + nums [r]
                    if diff > 0:
                        r-=1
                    elif diff <0:
                        l +=1
                    else:
                        results.append([n,nums[l],nums[r]])
                        l+=1
                        while nums[l] == nums[l+1] and l < r:
                             l+1
          return results 
                          





if __name__ =="__main__":
    nums=[-1,0,1,2,-1,-4]
    temp = ThreePointer()
    res = temp.threeSum(nums)
    print(res)
    
