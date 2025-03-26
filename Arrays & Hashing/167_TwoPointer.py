'''
probelm Two sum II in two approachs 
    1) Two Pointer Approach 
    2) Binary Search with | Time Complexity - o(n.log.n) & Space Complexity O(1) constant space 
'''

class TwoPointer:
    '''
    Two Pointer Technique in the soted arrya 
    '''
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0, len(numbers)-1
        while l < r:
            diff = numbers[l] + numbers[r]
            if diff > target:
                r-=1
            elif diff < target:
                l+=1
            else:
                return [l+1,r+1]
        return []
    
    def twosum_bs(self, nums:list[int], target: int) -> list[int]:
        print("Executing the Binary Search approach")
        for i in range(len(nums)-1):
            l,r = i+1, len(nums)-1
            temp = target - nums[i]
            while l<=r:
                mid = l + (r - l)//2
                if nums[mid] == temp:
                    return [i+1,mid+1]
                elif nums[mid] < temp:
                    l = mid+1
                else:
                    r = mid-1
        return []





if __name__ =="__main__":
    classcall = TwoPointer()
    inputnums = [1,2,3,4]
    target = 3
    result = classcall.twosum_bs(inputnums,target)
    print(result)