# Initial participant 
participants = 1 
# Each participant convinces 2 new people for 5 days 
growth_factor = 2 
days = 5 
# Calculate total participants after 5 days 
total_participants = participants * (growth_factor ** days) 
# Print the result 
print(f"Total participants after 5 days: {total_participants}")     