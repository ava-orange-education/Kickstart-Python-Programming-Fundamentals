# Step 2: Input
sandwich_type = input("What type of sandwich do you want? (PB&J or Ham): ")

# Step 3: Decision
toasted = input("Do you want it toasted? (yes or no): ").lower()

if toasted == "yes":
    print(f"Toasting the bread for your {sandwich_type} sandwich...")

# Step 4: Process
if sandwich_type.lower() == "pb&j":
    print("Adding peanut butter and jelly.")
elif sandwich_type.lower() == "ham":
    print("Adding ham and cheese.")

# Step 5: Output
print("Your sandwich is ready!")

# Step 6: End
