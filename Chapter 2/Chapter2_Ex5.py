Question Chapter 2 Exercise 5.
#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.
"""
"""
Explanation:
#This code first calculates how many USB sticks she can buy by using integer division (//) to divide her total budget by the cost of one USB stick. Then, it calculates how many pounds she will have left by using the modulo operator (%) 
#to find the remainder of the budget after buying as many USB sticks as possible. Finally, it prints the results.
"""
#Code:
"""
# Cost of one USB stick and the total budget in pounds
usb_stick_price = 6
total_budget = 50

# Calculate how many USB sticks she can buy
usb_sticks_bought = total_budget // usb_stick_price

# Calculate how many pounds she will have left
remaining_budget = total_budget % usb_stick_price

# Display the results
print(f"She can buy {usb_sticks_bought} USB sticks.")
print(f"She will have £{remaining_budget} left.")
