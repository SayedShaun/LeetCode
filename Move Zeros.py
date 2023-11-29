def move_zeros(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1
    print(arr)

arr = [0, 1, 0]
move_zeros(arr)