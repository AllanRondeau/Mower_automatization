from entity.Garden import Garden
from entity.Point import Point
from entity.Mower import Mower

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
i = i+1
garden_coords = Point(arr_garden_cords[0], arr_garden_cords[1])
garden = Garden(garden_coords)

# isEmpty = False
# while not isEmpty:
