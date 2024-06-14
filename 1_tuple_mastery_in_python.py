# Task 1 Formatting Flight Itineraries

travel_tuple_list = []

def input_loop():
    global travel_tuple_list
    while True:
        traveler_name = input("What is the traveler's name: ")
        origin = input("Where are you departing from: ")
        destination = input("What is your destination: ")
        travel_tuple = (traveler_name, origin, destination)
        #print(travel_tuple)
        travel_tuple_list.append(travel_tuple)
        #print(travel_tuple_list) used print statements to check I was on the right track
        repeat_loop = input("Would you like to add another itinerary (Y/N): ")
        if repeat_loop.upper() == "Y":
            print("Previous itinerary added to list, please proceed with second itinerary")
            continue
        else:
            print("Thank you for adding travel itineraries.")
            break

def itinerary_format(travel_tuple_list):
    for index, travel_tuple in enumerate(travel_tuple_list, 1):
        print(f"Itinerary {index}: {travel_tuple[0]} - From {travel_tuple[1]} to {travel_tuple[2]}") 


input_loop()
itinerary_format(travel_tuple_list)

'''
For this solution I built two functions. The first was a while loop taking inputs that would populate a global list of tuples. That information
took travelers' names, destination and origins made it into a tuple and the appended those tuples to the global list before asking if it would continue taking additional tuples.
After that loop is broken and all of the traveler information is added the resulting global list is the argument we will pass through our second function that unpacks an enumeration of this list.
The second function is a simple for loop were at each index in the list we number what itinerary number it is and then one by one access each index of each tuple while printing the travel details for those travelers.
'''