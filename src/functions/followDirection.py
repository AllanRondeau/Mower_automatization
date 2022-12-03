def follow_direction(arr, mower):
    arr_direction = ["N", "E", "S", "W"]
    y = 0
    direction = mower.get_direction()
    while y <= len(arr) - 1:
        i = 0
        # Stop when array value is equal to the mower direction and keep the index
        while arr_direction[i] != direction:
            i = i + 1
        # when mower has to turn left, it moves for 90° on the left. On cardinal point, you're turning like N ->W->S->E
        # Array is following clockwise for cardinal point, just have to move index at the inverse
        if arr[y] == "G":
            i = i - 1
            if i < 0:
                i = len(arr_direction) - 1

        if arr[y] == 'A':
            i = i

        if arr[y] == 'D':
            i = i + 1
            if i > len(arr_direction) - 1:
                i = 0

        direction = arr_direction[i]
        y = y + 1
    return direction
