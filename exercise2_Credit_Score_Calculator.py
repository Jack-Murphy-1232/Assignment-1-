score = int(input("What is your credit score? "))
if score < 300 or score > 850:
    print("Invalid Score")

elif score >= 750:
    print("Excellent - loan approved, low interest rate")

elif score >= 700 and score < 750:
    print("Good - loan approved with review, low interest rate")

elif score >= 600 and score < 700:
    print("Fair - loan conditional - seek credit improvement")

else: 
    print("Poor - loan denied")