def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def get_input_and_sort():
    print("--- Bubble Sort Algorithm ---")
    input_str = input("Please Input Number (with space) : ")
    
    try:
        data_to_sort = list(map(int, input_str.split()))
        
    except ValueError:
        print("Error: Input must be only numbers separated by spaces.")
        return

    print(f"\n Input: {data_to_sort}")
    sorted_result = bubble_sort(data_to_sort)  
    
    print(f"Bubble Sort: {sorted_result}")

if _name_ == "_main_":
    get_input_and_sort()