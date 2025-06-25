def display_contacts(contacts):
    """Display all contacts."""
    for name, phone in contacts.items():
        print(f"{name}: {phone}")