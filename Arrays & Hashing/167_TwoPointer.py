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

if __name__ =="__main__":
    classcall = TwoPointer()
    inputnums = [[2,7,11,15]]
    target = 9
    result = classcall.twoSum(inputnums,target)
    print(result)