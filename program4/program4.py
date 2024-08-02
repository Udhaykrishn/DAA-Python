import timeit
import random
import matplotlib.pyplot as plt

def input_array(n):
    array = []
    for _ in range(n):
        ele = random.randint(1, 50)
        array.append(ele)
    return array

def selection_sort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]

def main():
    N = []
    cpu = []

    trials = int(input("Enter the number of trials: "))
    for t in range(trials):
        array = []
        print(f"\nTRIAL NO: {t + 1}")
        n = int(input("Enter the number of elements: "))
        
        array = input_array(n)
        
        start = timeit.default_timer()
        selection_sort(array, n)
        times = timeit.default_timer() - start
        
        print("Sorted Array:")
        print(array)
        
        N.append(n)
        cpu.append(round(float(times) * 1000000, 2))
    
    print("N   CPU")
    for t in range(trials):
        print(N[t], cpu[t])
    
    plt.plot(N, cpu)
    plt.scatter(N, cpu, color="red", marker="x")
    plt.xlabel("Array size - N")
    plt.ylabel("CPU processing time (microseconds)")
    plt.title("Selection Sort Time Efficiency")
    plt.show()

if __name__ == "__main__":
    main()
