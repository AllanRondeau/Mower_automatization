def follow_direction(arr):
    # arr_direction = ["N", "E", "S", "W"]
    for y in range(len(arr)):
        return arr[y]

        # i = 0
        # # Stop when array value is equal to the mower direction and keep the index
        # while arr_direction[i] != mower.get_direction():
        #     i = i + 1

        # when mower has to turn left, it moves for 90° on the left. On cardinal point, you're turning like N ->W->S->E
        # Array is following clockwise for cardinal point, just have to move index at the inverse
        # if arr[y] == "G":
        #     i = i - 1
        #     if i < 0:
        #         i = len(arr_direction)
        #     mower = mower.set_direction(arr_direction[i])
        #
        # if arr[y] == "A":
        #     i = i
        #
        # if arr[y] == "D":
        #     i = i + 1
        #     if i > len(arr_direction):
        #         i = 0
        #     mower = mower.set_direction(arr_direction[i])
        # # return mower.get_direction()
