"""
01  Two pointer array - 
    Using Hashmap 
    

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap ={}
        for i, n in enumerate(nums):
            diff = target-n
            if diff in hashMap:
                return hashMap[diff], i
            hashMap[n] = i
        return 
        

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    NameClass = Solution()
    res1,res2 = NameClass.twoSum(nums,target)
    print(res1,res2)
