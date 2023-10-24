def counting_sort(arr):
    if len(arr) == 0:
        return arr

    # Find the minimum and maximum values in the input array
    min_val, max_val = min(arr), max(arr)
    
    # Create a counting array to store the frequency of each element
    count = [0] * (max_val - min_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct the sorted array from the counting array
    sorted_arr = []
    for i, count_i in enumerate(count):
        sorted_arr.extend([i + min_val] * count_i)
    
    return sorted_arr

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the counting_sort function to sort the list
    sorted_list = counting_sort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", sorted_list)

if _name_ == "_main_":
    main()
