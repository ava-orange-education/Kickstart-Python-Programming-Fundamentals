savings = 0 
monthly_saving = 200 
# January: Basic assignment for initial savings
savings = monthly_saving 
print(f"Savings after January: ${savings}") 
# February: Add and assign to include February's savings 
savings += monthly_saving # Equivalent to savings = savings + monthly_saving 
print(f"Savings after February: ${savings}") 
# March: Received a bonus, deciding to save more 
bonus_saving = 300 
savings += bonus_saving 
# Adjusting savings for March 
print(f"Savings after March with bonus: ${savings}") 
# April: Unexpected expense, need to adjust the saving goal
unexpected_expense = 100 
savings -= unexpected_expense 
# Adjusting savings for April 
print(f"Savings after April with expense: ${savings}") 
# May: Decide to double the monthly saving 
savings *= 2 # Doubling the savings for May 
print(f"Savings after May with double saving: ${savings}")      