my_string = "Python es increible"
space_index = my_string.find(' ')
first_word = my_string[:space_index]
first_word_upper = first_word.upper()
rest_of_string = my_string[space_index:]
new_string = first_word_upper + rest_of_string
print(new_string)