def get_tax_bracket(income):
    if income < 0:
        return "Invalid income amount."
    
    if income < 50_000:
        bracket = "low (10%)"
    elif 50_000 <= income < 100_000:
        bracket = "Medium (20%)" 
    elif income >= 100_000:
        bracket = "High (30%)"
    
    # Bonus 
    return bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket


income = float(input("What is your annual income "))
bracket = get_tax_bracket(income)
if bracket != "Invalid income amount.":
    if "(10%)" in bracket:
        tax = income * 0.10
    elif "(20%)" in bracket:
        tax = income * 0.20
    else:
        tax = income * 0.30
    print(f"Your tax bracket is: {bracket}. Estimated tax: ${tax:,.2f}")
else:
    print(bracket)