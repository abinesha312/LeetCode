'''
13_TapWater Porblem - 
     Using the Two Pointers in the given set of numbers
     check the max and min values for the number 
     followed by calculated the width of the Capacity 
'''


class solution(object):
    def TapWater(self,height):
        M_A = 0
        i,j=0,len(height)-1
        while i < j:
            capacity = (j-i) * min(height[i],height[j])
            M_A=max(M_A,capacity)

            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return M_A





if __name__ =="__main__":
    height =[1,8,6,2,5,4,8,3,7]
    call_MainFn = solution()
    result = call_MainFn.TapWater(height)
    print(result)
