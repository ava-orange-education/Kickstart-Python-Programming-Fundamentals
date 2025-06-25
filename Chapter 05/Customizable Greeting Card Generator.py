def create_greeting_card(occasion="Birthday", recipient="Friend", *messages, **details): 
    print(f"Happy {occasion}, {recipient}!") 
    for message in messages: 
        print(f"- {message}") 
        for key, value in details.items(): 
            print(f"{key}: {value}") 
# Example function call 
create_greeting_card("Birthday", "Alice", "Wishing you all the best", 
                     "Here's to another great year!", sender="Bob", date="2024-04-01")
