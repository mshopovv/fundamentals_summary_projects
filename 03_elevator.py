from math import ceil

all_people = int(input())
capacity_elevator = int(input())

number_of_lifts = ceil(all_people / capacity_elevator)

print(number_of_lifts)