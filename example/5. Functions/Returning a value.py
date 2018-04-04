# Function to calculate tax and return the total
def calculateTax(price, tax_rate):
    total = price + (price*tax_rate)
    my_price = 200
    print("My_price = ", my_price)
    return total                        # return the total

my_price = float(input("Enter a price: "))

# Call the function and store the result in totalPrice
totalPrice = calculateTax(my_price, 0.06)

print("price = ", my_price, " Total price = ", totalPrice)
