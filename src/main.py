from entity.Garden import Garden
from entity.Point import Point
from entity.Mower import Mower
from functions.parseCoords import parse_coords
from functions.parseInstruction import parse_instruction
from functions.followDirection import follow_direction

# Define an empty list
places = []
i = 0

# Open the file and read the content in a list
with open('../husqvarna.dat', 'r') as filehandle:
    for line in filehandle:
        # Remove linebreak which is the last character of the string
        curr_place = line[:-1]
        # Add item to the list
        places.append(curr_place)

# Create garden object with coord point.
arr_garden_cords = [int(x) for x in str(places[i])]
garden_coords = Point(arr_garden_cords[0], arr_garden_cords[1])
garden = Garden(garden_coords)

isEmpty = False
garden_mower = None
while not isEmpty:
    i = i + 1
    # try to resolve instruction related to places array
    try:
        if i % 2 != 0:
            arr = parse_coords(places[i])
            point = Point(arr[0], arr[1])
            mower = Mower(point, arr[3])
            garden.set_mower(mower)
            garden_mower = garden.get_mower()
            print(garden_mower.get_direction())

        if i % 2 == 0:
            arr_parse_direction = parse_instruction(places[i])
            print(arr_parse_direction)
            direction = follow_direction(arr_parse_direction)
            print(direction)

    # Exception when an error occurred because of the emptiness of the array. Stop the while.
    except:
        print("there's no more to go")
        isEmpty = True
