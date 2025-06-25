total_budget = 150
decor_cost = 40
snack_cost_per_pack = 5
cake_cost = 20
guests = 10
# Calculate remaining budget after buying decorations and a cake
remaining_budget = total_budget - (decor_cost + cake_cost)
# Determine the number of snack packs to buy (one for each guest)
snack_packs_needed = guests
total_snack_cost = snack_cost_per_pack * snack_packs_needed
# Update remaining budget after buying snacks
remaining_budget -= total_snack_cost
# Party hats calculation (packs of 5)
hats_per_pack = 5
packs_needed = guests // hats_per_pack + (guests % hats_per_pack > 0)
# Ensuring every guest gets a hat
# Balloons calculation (using exponentiation for fun)
balloon_sets_needed = 2
# Deciding on 2 sets for simplicity
balloons_per_set = 2**2
# Each set contains 2^2 = 4 balloons
total_balloons = balloon_sets_needed * balloons_per_set
# Display results
print(f"Remaining budget after purchases: ${remaining_budget}") 
print(f"Total snack packs needed: {snack_packs_needed}")
print(f"Total packs of party hats needed: {packs_needed}")
print(f"Total balloons for decoration: {total_balloons}")