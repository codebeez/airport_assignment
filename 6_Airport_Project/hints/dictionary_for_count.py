"""
We use a dictionary to accumulate the count of reccuring destination phone numbers of telephone calls.
"""
from collections import defaultdict

# format: source_number, destination_number
telephone_calls = [[123, 321], [333, 321], [123, 333], [333, 123], [123, 321]]

routing_count = {}
for telephone_call in telephone_calls:
    source_number, destination_number = telephone_call

    if destination_number in routing_count:
        routing_count[destination_number] += 1
    else:
        routing_count[destination_number] = 1

print(routing_count)

"""
Advanced: Use collections.defaultdict to ease the counting
"""


def default():
    return 0


routing_count = defaultdict(default)
for telephone_call in telephone_calls:
    source_number, destination_number = telephone_call
    routing_count[destination_number] += 1

print(routing_count)
