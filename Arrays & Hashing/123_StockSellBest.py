class solution:
    '''
    Technique : Two Pointer
    Time Complexity : O(n)
    Space Complexity : O(1)
    Remarks: Make significant improvement
    '''
    def SellStock_Tp(int,prices:list[int])->list[int]:
        l,r = 0,1
        mp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                current_Profit = prices[r] - prices[l]
                mp = max(current_Profit,mp)
            else:
                l=r
            r+=1
        return mp





    '''
    Technique : Brute force
    Time Complexity : O(n*2)
    Space Complexity :O(1)
    Remarks: Not an efficent method it will work
    '''
    def SellStock_Brt(self, prices: list[int])->list[int]:
        print("Brute force Approach")
        res = 0 
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                res = max(res,sell - buy)
        return res







if __name__ =='__main__':
    cCall = solution()
    prices = [7,1,5,3,6,4]
    val = cCall.SellStock_Tp(prices)
    print(val)

