from entity.Garden import Garden
from entity.Point import Point
from entity.Mower import Mower
from functions.parseCoords import parse_coords
from functions.parseInstruction import parse_instruction
from functions.followDirection import follow_direction

# Define an empty list
places = []
ind = 0

# Open the file and read the content in a list
with open('../husqvarna.dat', 'r') as filehandle:
    for line in filehandle:
        # Remove linebreak which is the last character of the string
        curr_place = line[:-1]
        # Add item to the list
        places.append(curr_place)
# Create garden object with coord point.
arr_garden_cords = [int(x) for x in str(places[ind])]
garden_coords = Point(arr_garden_cords[0], arr_garden_cords[1])
garden = Garden(garden_coords)

isEmpty = False
garden_mower = None

i = 0
mower_position = []

while not isEmpty:
    ind = ind + 1
    # try to resolve instruction related to places array
    try:
        if ind <= len(places) - 1:
            if ind % 2 != 0:
                arr_parse_coords = parse_coords(places[ind])
                point = Point(arr_parse_coords[0], arr_parse_coords[1])
                mower = Mower(point, arr_parse_coords[3])
                garden.set_mower(mower)
                garden_mower = garden.get_mower()

            if ind % 2 == 0:
                arr_parse_direction = parse_instruction(places[ind]) # Parse all instruction in an array
                # return the mower with his final position after his work done.
                mower = follow_direction(arr_parse_direction, garden_mower, garden)
                print(mower.create_point_with_card_dir()) # Display his final position.
        # Stop the while when array is empty.
        else:
            isEmpty = True
    except ValueError:  # Exception when an error occurred.
        print("there's no more to go")
        isEmpty = True
