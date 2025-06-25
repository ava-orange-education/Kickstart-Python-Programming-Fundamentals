last_year_members = {'John', 'Mary', 'Steve', 'Olivia'} 
this_year_members = {'Mary', 'Steve', 'James'} 
non_renewed_members = last_year_members.difference(this_year_members) 
print(non_renewed_members) # Outputs {'John', 'Olivia'} 
