import math

# Type your code here.
    #      0          1          2
days = ["Friday", "Saturday", "Sunday"]
wkndTotal = 0
# vars will go as follows: People, slices per person, cost of one pizza
for i in range (0,3):
    vars = input("").split(" ")

    numPeople = int(vars[0])
    numSlicePer = float(vars[1])
    costPerPizza = float(vars[2])
    print(str(days[i]) + " Night Party")
    numPizzas = math.ceil( (numPeople * numSlicePer) / 8)
    price = costPerPizza * numPizzas
    taxes = price * 0.07
    deliveryFee = (price + taxes) * 0.2
    total = price + taxes + deliveryFee
    wkndTotal = wkndTotal + total

    print(f"{numPizzas} Pizzas: ${price:.2f}")
    print(f"Tax: ${taxes:.2f}")
    print(f"Delivery: ${deliveryFee:.2f}")
    print(f"Total: ${total:.2f}")
    print("")

print(f"Weekend Total: ${wkndTotal:.2f}")


# Did not work, got an error when trying to input info. 8/10, missing steps 4/5 to confirm