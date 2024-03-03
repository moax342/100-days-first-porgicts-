array_unsorted = input("Enter the numbers that you want to be sorted from \n").split(",")


new_list = []
list_size = len(array_unsorted)

# sort a list from maximum to minimum
while list_size != 0:
    initial_number = 0
    for item in range(0, list_size):
        # take the number that wanted to be cheeked from the list and turn it ito integer
        checked_number = int(array_unsorted[item])
        # check the number against the list of numbers
        if checked_number > initial_number:
            initial_number=checked_number
    # adding the number to the list to be sorted
    new_list.append(initial_number)
    # removing the number from the old list
    array_unsorted.remove(str(initial_number))
    list_size -= 1

print(new_list)
