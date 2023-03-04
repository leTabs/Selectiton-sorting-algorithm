# selection sorting algorithm
def selection_sorting(array):
    for item in range(len(array)):
        # looping as many times as the total amount of items stored in the array
        min_item = min(array[item:])
        # identifying the smallest item inside the unsorted part of the array
        min_index = array.index(min_item, item)
        # finding it's index
        if min_item < array[item]:
            # if smallest item in the unsorted array is smallest than the current one
            # according to the loops item, those two swich places
            array[item] , array[min_index] = array[min_index], array[item]
            # thus, the array forms the correct ascending order
    return array
    # the function return the array after the loop is finished

test_array = [3,1,6,2,3,9,1,-2,3,9,-9]
print(selection_sorting(test_array))
# output: [-9, -2, 1, 1, 2, 3, 3, 3, 6, 9, 9]
