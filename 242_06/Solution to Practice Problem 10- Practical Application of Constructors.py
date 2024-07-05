class UserProfile: 
    def __init__(self, username, email, location="Not specified"): 
        self.username = username 
        self.email = email 
        self.location = location 
    def update_email(self, new_email): 
        self.email = new_email 
    def update_location(self, new_location): 
        self.location = new_location 
    def display_profile(self): 
        return f"Username: {self.username}, Email: {self.email}, Location: {self.location}" 
    
# Test the code 
user_profile = UserProfile("john_doe", "john@example.com") 
print(user_profile.display_profile()) # Outputs: Username: john_doe, Email: john@example.com, Location: Not specified 
user_profile.update_email("new_john@example.com") 
user_profile.update_location("New York") 
print(user_profile.display_profile()) # Outputs: Username: john_doe, Email: new_john@example.com, Location: New York