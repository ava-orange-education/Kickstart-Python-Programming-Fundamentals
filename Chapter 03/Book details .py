book1_name = "Journey Through Python" 
book1_pages = 350 
book2_name = "Data Science Expedition" 
book2_pages = 250 
# Average pages in a programming book 
average_pages = 300 
# Greater than: Is book1 longer than the average?
is_book1_longer_than_average = book1_pages > average_pages 
# Less than: Is book2 shorter than the average?
is_book2_shorter_than_average = book2_pages < average_pages 
# Equal to: Do both books have the same number of pages?
are_books_equal_in_length = book1_pages == book2_pages 
# Not equal to: Are the books different in length?
are_books_different_in_length = book1_pages != book2_pages
# Greater than or equal to: Is book1 as long or longer than book2?
is_book1_as_long_or_longer_than_book2 = book1_pages >= book2_pages 
# Less than or equal to: Is book2 as short or shorter than book1? 
is_book2_as_short_or_shorter_than_book1 = book2_pages <= book1_pages 
# Displaying the results 
print(f"Is '{book1_name}' longer than the average programming book? {is_book1_longer_than_average}") 
print(f"Is '{book2_name}' shorter than the average programming book? {is_book2_shorter_than_average}") 
print(f"Do '{book1_name}' and '{book2_name}' have the same number of pages? {are_books_equal_in_length}") 
print(f"Are '{book1_name}' and '{book2_name}' different in length? {are_books_different_in_length}") 
print(f"Is '{book1_name}' as long or longer than '{book2_name}'? {is_book1_as_long_or_longer_than_book2}") 
print(f"Is '{book2_name}' as short or shorter than '{book1_name}'? {is_book2_as_short_or_shorter_than_book1}")  