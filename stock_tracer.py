stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}

total = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        investment = stocks[stock] * qty
        total += investment
        print("Investment for", stock, "=", investment)
    else:
        print("Stock not found")

print("Total Portfolio Value =", total)

file = open("portfolio.txt", "w")
file.write("Total Portfolio Value = " + str(total))
file.close()

print("Result saved in portfolio.txt")