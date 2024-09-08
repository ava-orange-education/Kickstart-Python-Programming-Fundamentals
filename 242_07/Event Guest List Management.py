# Set for all invited guests 
invited = set(input("Enter invited guests (comma-separated): ").split(',')) 
# Set for guests who RSVP'd 
rsvped = set(input("Enter guests who RSVP'd (comma-separated): ").split(',')) 
# Set for guests who actually attended \
attended = set(input("Enter guests who attended (comma-separated): ").split(',')) 

# Guests who RSVP'd but did not attend 
no_shows = rsvped - attended 
print("RSVP'd but did not attend:", no_shows) 

# Guests who attended without RSVP'ing 
unexpected_guests = attended - rsvped 
print("Attended without RSVP:", unexpected_guests) 

# Guests who RSVP'd and attended 
confirmed_guests = rsvped & attended 
print("RSVP'd and attended:", confirmed_guests) 
