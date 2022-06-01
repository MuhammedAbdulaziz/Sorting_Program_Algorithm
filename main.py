import random
import time

swapCountM, stmtCountM, compCountM = 0, 0, 0
swapCountQ, stmtCountQ, compCountQ = 0, 0, 0
swapCountH, stmtCountH, compCountH = 0, 0, 0


def merge_sort(arr):
    global stmtCountM, compCountM, swapCountM

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                stmtCountM += 1
            else:
                arr[k] = R[j]
                j += 1
                swapCountM += 1
                compCountM += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            stmtCountM += 1
            swapCountM += 1
            compCountM += 1
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            stmtCountM += 1
            swapCountM += 1
            compCountM += 1
            j += 1
            k += 1


def partition(l, r, nums):
    global stmtCountQ, compCountQ, swapCountQ
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            compCountQ += 1
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            swapCountQ += 1
            ptr += 1

    # Finally, swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    swapCountQ += 1
    return ptr


def quicksort(l, r, nums):
    global compCountQ
    if len(nums) == 1:
        compCountQ += 1  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        compCountQ += 1
        pi = partition(l, r, nums)
        quicksort(l, pi - 1, nums)  # Recursively sorting the left values
        quicksort(pi + 1, r, nums)  # Recursively sorting the right values
    return nums


def heapify(arr, n, i):
    global stmtCountH, compCountH, swapCountH
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    stmtCountH += 2
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        compCountH += 2
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        compCountH += 2
        stmtCountH += 1
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        compCountH += 2
        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heap_sort(arr):
    global swapCountH
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swapCountH += 1  # swap
        heapify(arr, i, 0)


def sorting_option_menu(random_list):
    while True:
        operation = input('''
Select operation:
    1.Merge Sort
    2.Heap Sort
    3.Quick Sort
    4.All of them
    5.Exit/Quit
        ''')
        if operation == '1':
            start_time = time.time()
            merge_sort(arr=random_list)
            print(random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in MergeSort'.format(stmtCountM,
                                                                                                          swapCountM,
                                                                                                          compCountM))
            print(' Time Taken = %s Seconds ' % (time.time() - start_time))
            break

        elif operation == '2':
            start_time = time.time()
            heap_sort(random_list)
            print(random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in Heap Sort'.format(stmtCountH,
                                                                                                          swapCountH,
                                                                                                          compCountH))
            print(' Time Taken = %s Seconds ' % (time.time() - start_time))
            break

        elif operation == '3':
            start_time = time.time()
            quicksort(0, len(random_list) - 1, random_list)
            print(random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in Quick Sort'.format(stmtCountQ,
                                                                                                           swapCountQ,
                                                                                                           compCountQ))
            print(' Time Taken = %s Seconds ' % (time.time() - start_time))
            break

        elif operation == '4':
            start_time = time.time()
            merge_sort(arr=random_list)
            print('=====================================================')
            print(' Merge Sort = ', random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in MergeSort'.format(stmtCountM,
                                                                                                          swapCountM,
                                                                                                          compCountM))
            print(' Time Taken By Merge = %s Seconds ' % (time.time() - start_time))
            start_time = time.time()
            heap_sort(random_list)
            print('=====================================================')
            print(' Heap Sort = ', random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in Heap Sort'.format(stmtCountH,
                                                                                                          swapCountH,
                                                                                                          compCountH))
            print(' Time Taken By Heap = %s Seconds ' % (time.time() - start_time))
            start_time = time.time()
            quicksort(0, len(random_list) - 1, random_list)
            print('=====================================================')
            print(' Quick Sort = ', random_list)
            print(' Statement Count = {} \n Swap Count = {} \n Comparison Count = {} in Quick Sort'.format(stmtCountQ,
                                                                                                           swapCountQ,
                                                                                                           compCountQ))
            print(' Time Taken By Quick = %s Seconds ' % (time.time() - start_time))
            print('=====================================================')
            break

        elif operation == '5':
            print("\nExiting....")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        operation = input('''
Select operation:
    1.Sorted list
    2.Inversely Sorted List
    3.Random List
    4.Exit/Quit
''')
        if operation == '1':
            random_list = random.sample(range(10, 300), 50)
            random_list.sort()
            print(random_list)
            sorting_option_menu(random_list)

        elif operation == '2':
            random_list = random.sample(range(10, 300), 50)
            random_list.sort(reverse=True)
            print(random_list)
            sorting_option_menu(random_list)

        elif operation == '3':
            random_list = random.sample(range(10, 300), 50)
            print(random_list)
            sorting_option_menu(random_list)

        elif operation == '4':
            print("\nExiting....")
            break

        else:
            print("Invalid choice. Please try again.")


main()
