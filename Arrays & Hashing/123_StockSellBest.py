class solution:
    '''
        Diffculty leve : Easy
        Best time to sell stock value.
    '''
    def SellStock(int,prices:list[int])->list[int]:
        l,r = 0,1
        maxVa = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                maxVa = max(profit,maxVa)
                # maxVa = diff
            else:
                l = r
            r+=1
        return maxVa                


if __name__ =='__main__':
    cCall = solution()
    prices = [7,1,5,3,6,4]
    val = cCall.SellStock(prices)
    print(val)

