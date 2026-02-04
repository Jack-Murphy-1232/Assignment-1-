#Exercise 1: Profit Margin Calculator with float inputs


revenue = float(input("What is the revenue? "))
cost = float(input("What is the cost? "))

Profit = revenue - cost

if revenue > 0: 
    Margin = (Profit / revenue) * 100
    print(f"profit: ${Profit:,.2f}")
    print(f"margin: {Margin:.2f}%")


else:
    print("Invalid revenue amount.")