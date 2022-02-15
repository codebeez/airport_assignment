"""
Here we are parsing individual lines of the dataset.
We are interested in the destination airport.
"""

line = "2B,410,DME,4029,NBC,6969,,0,CR2"
elements = line.split(",")

print(elements)  # notice how the missing value is represented by an empty string ''

destination_code = elements[4]
destination_id = elements[5]

print("destination_code", destination_code)
print("destination_id", destination_id)
