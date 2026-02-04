def is_profitable(revenue, cost):
    return revenue > cost

def main():
    revenue = float(input("Revenue:"))
    cost = float(input("Cost: "))
    product = input("Product Category: ").strip().lower()
    if is_profitable(revenue, cost):
        match product:
            case "electronics" | "gadget" | "tech":
                category = "High Margin"
            case "clothing" | "apparel":
                category = "Medium Margin"
            case "food" | "grocery":
                category = "Low Margin"
            case _:
                category = "Manual Review Required"
                profit = revenue - cost
                if profit > 0:
                    advice = "Consider investing more resources."
                else:
                    advice = "Avoid investing in this product."
                print (f"Profit: ${profit:.2f}")
                print (f"Suggestion: {advice}")
        
            


main()
