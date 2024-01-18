#task No 3(D)
def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    # Sorting to compare both lists and compare
    list1.sort()
    list2.sort()
    
    return list1 == list2


list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1,]

if are_lists_equal(list1, list2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")
