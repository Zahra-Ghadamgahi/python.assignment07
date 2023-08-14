def is_sorted(lst):
    return lst == sorted(lst)

user_input = input("Enter the elements of the list(space_seprated): ")
lst = [int(element) for element in user_input.split()]

if is_sorted(lst):
    print("the list is sorted in ascending order.")
else:
    print("the list is not sorted in ascending order.")

is_sorted(lst)