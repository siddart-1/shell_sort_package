# shell_sort/shell_sort.py

def shell_sort(arr):
    """
    Sorts an array using the shell sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def get_user_input():
    """
    Gets a list of numbers from the user.

    Returns:
        list: A list of numbers.
    """
    user_input = input("Enter a list of numbers separated by spaces: ")
    try:
        numbers = [float(num) for num in user_input.split()]
        return numbers
    except ValueError:
        print("Invalid input. Please enter a list of numbers separated by spaces.")
        return get_user_input()


def main():
    numbers = get_user_input()
    sorted_numbers = shell_sort(numbers)
    print("Sorted numbers:", sorted_numbers)


if __name__ == "__main__":
    main()