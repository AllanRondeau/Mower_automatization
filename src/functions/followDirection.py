def follow_direction(arr, mower, garden):
    arr_direction = ["N", "E", "S", "W"]
    y = 0
    direction = mower.get_direction()
    while y <= len(arr) - 1:
        i = 0
        # Stop when array value is equal to the mower direction and keep the index
        while arr_direction[i] != direction:
            i = i + 1

        # when mower has to turn, it moves for 90° on the side. On cardinal point, you're turning like N ->W->S->E
        # Array is following clockwise for cardinal point.
        # To turn on the left, just have to read the array in descending.
        if arr[y] == "G":
            i = i - 1
            if i < 0:
                i = len(arr_direction) - 1

        if arr[y] == 'A':
            i = i

        # Follow the clockwise, read array in ascending
        if arr[y] == 'D':
            i = i + 1
            if i > len(arr_direction) - 1:
                i = 0

        # direction var take the
        direction = arr_direction[i]

        # +1 on ordinate
        if direction == "N" and arr[y] == "A":
            point = int(mower.get_point_y()) + 1
            if point <= int(garden.get_point_y()):
                mower.set_point_y(point)
        # - 1 on abscissa
        if direction == "W" and arr[y] == "A":
            point = int(mower.get_point_x()) - 1
            if point > 0:
                mower.set_point_x(point)
        # - 1 on ordinate
        if direction == "S" and arr[y] == "A":
            point = int(mower.get_point_y()) - 1
            if point > 0:
                mower.set_point_y(point)
        # + 1 on abscissa
        if direction == "E" and arr[y] == "A":
            point = int(mower.get_point_x()) + 1
            if point <= int(garden.get_point_x()):
                mower.set_point_x(point)

        y = y + 1

    # Set cardinal orientation to the mower.
    mower.set_direction(direction)
    return mower
