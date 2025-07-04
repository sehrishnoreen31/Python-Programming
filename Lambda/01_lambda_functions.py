# square numbers
numbers = [5,6,4,3,2,5,3,2]
squared_numbers = list(map(lambda x:x**2, numbers))
print(squared_numbers)

# string concatination
str1 = 'Hello'
str2 = 'world'
concatenated_str =( lambda str_a, str_b: str_a + ' ' + str_b)(str1, str2)
print(concatenated_str)

# sort a list by second element
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)

# # sort a list by first element
# people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# sorted_people =  sorted(people) # by default it would take first element or use sorted(people, key=lambda person: person[0])
# print(sorted_people)

# filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

# Convert a List of Strings to Uppercase
strings = ['hello', 'world']
upper_strings = list(map(lambda a: a.upper(), strings))
print(upper_strings)

#  Sort a List of Dictionaries by a Key
students = [
    {'name': 'Ali', 'score': 88},
    {'name': 'Zara', 'score': 95},
    {'name': 'Omar', 'score': 75}
]
sorted_students = list(sorted(students, key=lambda a: a['score'], reverse=True))
print(sorted_students)

