class solution:
    def sortedArray(self, nums: list[int],target: int)->int:
        '''
            Goal - Time complexity if O(log.n)
            Note: 
                If we need less time complexity then we can use the binary search on a linear graph
        '''
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            # Checking the target value with the left part
            #  
            if nums[l] <= nums[mid]:
                print('Entering into the left side of the array',l)
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                print('Entering into the Right side of the array',r)
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1 
                    
if __name__ == '__main__':
    call = solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    val = call.sortedArray(nums,target)
    print('priting the index of the target value in the array', val)

