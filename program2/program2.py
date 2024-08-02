import time
import matplotlib.pyplot as plt

def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    n_values = []
    times = []
    r = int(input("Enter the number of runs: "))
    for _ in range(r):
        n = int(input("Enter the number of elements: "))
        arr = sorted(list(map(int, input("Enter the elements of the array: ").split())))
        key = int(input("Enter the key element to be searched: "))
        repeat = 10000
        
        start_time = time.time()
        for _ in range(repeat):
            result = binary_search(arr, 0, n-1, key)
        end_time = time.time()
        
        if result != -1:
            print(f"Key {key} found at position {result}")
        else:
            print(f"Key {key} not found")
        
        time_taken = (end_time - start_time) * 1000    # Time taken in milliseconds
        print(f"Time taken to search the key element: {time_taken} milliseconds\n")
        
        n_values.append(n)
        times.append(time_taken)
    
    # Plotting the results
    plt.figure()
    plt.plot(n_values, times, 'o-')
    plt.xlabel("Number of elements (n)")
    plt.ylabel("Time taken (milliseconds)")
    plt.title("Binary Search Time Complexity")
    plt.grid(True)
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
