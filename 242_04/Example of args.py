def describe_pet(name, *args, **kwargs): 
    print(f"Pet name: {name}") 
    for attribute in args: 
        print(f"- {attribute}") 
        for key, value in kwargs.items(): 
            print(f"- {key}: {value}") 
describe_pet("Fido", "dog", color="brown", age=5) 
