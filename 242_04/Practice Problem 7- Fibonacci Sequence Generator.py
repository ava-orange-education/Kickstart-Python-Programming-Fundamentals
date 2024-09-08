# Prompt the user for the number of terms in the Fibonacci sequence they wish to generate. 
n_terms = int(input("How many terms? ")) 
# Initialize the first two terms of the Fibonacci sequence. 
n1, n2 = 0, 1 
count = 0 
# Validate the number of terms. 
if n_terms <= 0: 
    print("Please enter a positive integer") 
elif n_terms == 1: 
    # If only one term is requested, print it directly. 
    print("Fibonacci sequence up to", n_terms, ":") 
    print(n1) 
else: 
    # Generate the Fibonacci sequence for the requested number of terms. 
    print("Fibonacci sequence:") 
    while count < n_terms: 
        print(n1) 
        # Update the terms for the next iteration. 
        nth = n1 + n2 
        n1 = n2 
        n2 = nth 
        count += 1
