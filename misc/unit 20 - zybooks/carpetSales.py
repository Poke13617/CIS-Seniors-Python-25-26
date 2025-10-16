# Type your code here.

# Original code:
#ppsf = float(input())
#roomW = int(input())
#roomL = int(input())
#roomArea = roomW * roomL
#cost = (ppsf * roomArea) * 1.2
#print("Room: " + str(roomArea) + " square feet")
#print(f"Cost: {cost:.2f}")

#laborCost = .75 * roomArea
#print(f"Labor: {laborCost:.2f}")

#tax = (laborCost + cost) * 0.07
#print(f"Tax: {tax:.2f}")

#Updated to work
order = 0
finalCost = 0
moreOrders = ""
for i in range(0,3):
    order = order + 1
    print("Order #" + str(order))
    ppsf = input("").split( )
    

    pricePerSqFt = float(ppsf[0])
    roomW = int(ppsf[1])
    roomL = int(ppsf[2])
    roomArea = roomW * roomL
    cost = (pricePerSqFt * roomArea) * 1.2
    print("Room: " + str(roomArea) + " sq ft")
    print(f"Carpet: ${cost:.2f}")

    laborCost = .75 * roomArea
    print(f"Labor: ${laborCost:.2f}")

    tax = (laborCost + cost) * 0.07
    total = laborCost + tax + cost
    finalCost = finalCost + total
    print(f"Tax: ${tax:.2f}")
    print(f"Cost: ${total:.2f}")
    print("")
    
    
print(f"Total Sales: ${finalCost:.2f}")