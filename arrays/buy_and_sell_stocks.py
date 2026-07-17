#  BUY AND SELL STOCK 

# brute force:

prices = [7,1,5,3,6,4]

max_profit=0
for i in range(len(prices)):
    profit=0
    for j in range(i+1,len(prices)):
        profit=prices[j]-prices[i]
        
        max_profit=max(max_profit,profit)
        
if max_profit<0:
    print(0)
else:
    print(max_profit)
    
    
    
# optimal approch 

prices = [7,1,5,3,6,4]
profit=0
max_profit=0
min_price=prices[0]
for i in range(1,len(prices)):
    min_price=min(min_price,prices[i])
    profit = prices[i]-min_price
    
    max_profit=max(max_profit,profit)

print(max_profit)
