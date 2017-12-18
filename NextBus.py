import requests
import json

def Main():


    def get_route_from_int(userRoute):
        # Getting the json
        formatURL = requests.get(routesURL)
        json_data = json.loads(formatURL.content)
        # Iterating through the data until a match is found
        for data in json_data:
            route = data["Route"]
            if route == userRoute:
                return route
        # Default return
        return "Invalid bus route"
    def get_route_from_string(userRoute):
        # Getting the json
        formatURL = requests.get(routesURL)
        json_data = json.loads(formatURL.content)
        # Iterating through the data until a match is found
        for data in json_data:
            route = data["Description"]
            if route == userRoute:
                return data["Route"]
        # Default return
        return "Invalid bus route"
    def get_direction(bus, direction):
        # Getting the json
        formatURL = requests.get(directionsURL.format(bus))
        json_data = json.loads(formatURL.content)
        # Iterating through the data until a match is found
        for data in json_data:
            text = data["Text"]
            # Formatting the return and input
            formatText = text[:-5]
            if formatText == direction.upper():
                return data["Value"]
        # Default return
        return "Selected bus does not go in this direction"
    def get_stops(route, direction, destination):
        # Getting the json
        formatURL = requests.get(stopsURL.format(route, direction))
        json_data = json.loads(formatURL.content)
        # Iterating through the data until a match is found
        for data in json_data:
            text = data["Text"]
            if text == destination:
                return data["Value"]
        # Default return
        return "Invalid stop"
    def get_next_bus(route, direction, stop):
        # Getting the json
        formatURL = requests.get(nextBusURL.format(route, direction, stop))
        json_data = json.loads(formatURL.content)
        # Checking the size of the json. If 0 returns default statement
        if len(json_data) == 0:
            print("No more buses for the day")
        # Returning the first item/earliest bus time
        else:
            bus = json_data[0]["DepartureText"]
            print("Next departure: " + bus)
    def check_length(argument):
        # Checking if the input is empty or not
        while len(argument) == 0:
            argument = input("Enter an argument:")
        return argument
    # Defining the base URLS
    routesURL = "http://svc.metrotransit.org/NexTrip/Routes?format=json"  # All routes
    stopsURL = "http://svc.metrotransit.org/NexTrip/Stops/{0}/{1}?format=json"  # Route,Direction
    directionsURL = "http://svc.metrotransit.org/NexTrip/Directions/{0}?format=json"  # Route
    nextBusURL = "http://svc.metrotransit.org/NexTrip/{0}/{1}/{2}?format=json"  # Route,Direction,Stop


    userRoute = check_length(input("Enter the bus route:\n"))
    # 2 different functions that run depending on if the input is a number


    if userRoute.isdigit():
        route = get_route_from_int(userRoute)

    else:
        route = get_route_from_string(userRoute)

    # east,south,west,north
    userDirection = check_length(input("Enter the bus direction:\n"))

    if route.isdigit():
        # Getting direction code based on the route and user input
        directions = get_direction(route, userDirection)

        destination = check_length(input("Enter your stop:\n"))

        if directions.isdigit():
            # Getting the stop code based on the route, direction and user input
            stop = get_stops(route, directions, destination)

            if len(stop) < 5:
                # Getting the results
                get_next_bus(route, directions, stop)
            # Catching Error
            else:
                print(stop)
    # Catching Error
    else:
        print(route)

Main()