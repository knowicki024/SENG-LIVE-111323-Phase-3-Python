# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = [ "Rose", "Cup", "Hammie", "Hazel", "Sadie", "Gigi", "Pinky", "Hammie", "Japhy", "Jappy"]

# Reading Information From Lists
#2. ✅ Return the first pet name 
print(pet_names[0])

#3. ✅ Return all pet names beginning from the 3rd index
print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index
print(pet_names[:3])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
print(pet_names[3:7])

#6. ✅ Find the index of a given element
print(pet_names.index('Gigi'))

#7. ✅ Reverse the original list
print(pet_names.reverse())
print(pet_names)

#8. ✅ Return the frequency of a given element 
print(pet_names.count("Hammie"))

# Updating Lists
#9. ✅ Change the first element to all uppercase 
pet_names[0] = pet_names[0].upper()
print(pet_names)

#10. ✅ Append a new name to the list
pet_names.append("Clementine")
print(pet_names)

#11. ✅ Add a new name at a specific index
pet_names.insert(3, "Ken")
print(pet_names)

#12. ✅ Add two lists together 
#option 1
new_list = ['winter', 'lucy']
combine_list = pet_names + new_list
print(combine_list)

#mutate the original list
new_list_2 = [1, 2, 3, 4] 
pet_names.extend(new_list_2)
print(pet_names)


#13. ✅ Remove the final element from the list
pet_names.pop()
print(pet_names)

#14. ✅ Remove element by specific index
print(pet_names.pop(6))
pet_names.remove(pet_names[6])

#15. ✅ Remove a specific element 
pet_names.remove("Rose")
print(pet_names)

#16. ✅ Remove all pet names from the list
pet_names.clear()

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable
    # List : Mutable
    # Tuple : Immutable

# Tuple is an immutable data type that can also store many types of data.

#17. ✅ Create a Tuple of pet 10 ages 
pet_ages = ( 1, 2, 3, 4, 5, 6, 7, 7, 7, 7 )

#18. ✅ Print the first pet age
pet_ages[0]

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)


#20. ✅ Attempt to change the first element (should error)


# Tuple Methods
#21. ✅ Return the frequency of a given element
pet_ages.count(7)

#22. ✅ Return the index of a given element 
print(pet_ages.index(5))



#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops


# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info = { "name": "Hammurabi", "age": "8 months", "breed": "golden doodle"}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_2 = dict(name="Hazel", age=2, breed="labdoodle")


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 


#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error


# Updating 
#29. ✅ Update the pets age to 12


#30. ✅ Update the other pets age to 26


# Deleting
#30. ✅ Delete a pets age using the "del" keyword 


#31. ✅ Delete the other pets age using ".pop"


#32. ✅ Delete the last item in the pet dictionary using "popitem()"


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range


#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number


#35. ✅ Loop through the "pet_info" list and print every dictionary 


#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument


#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 


#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'


# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase


# find like
#40. ✅ Use list comprehension to find a pet named spot


# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old


#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
