


# Train car stuff
car =
    { maximumCapacity = M
    , safeCapacitcy = N
    , spaces = 2D N x (M/N)
    }

M = 20
N = 4

# For the L-line, a train car's capacity is:
# For the L-line, there are 8 cars per train.
M = 258
N = 20

# A sample vector of lists,
# X: uninfected passenger
# I: infected passenger
# [ [I,X] 
# , [X]
# , []
# , [X]
# ]


# Passenger stuff
passenger =
    { stopsUntilDisembark = Int
    , exposureTime = (Int, minutes exposed)
    , rideTime = Int
    , infected = Boolean
    }

# Station
station =
    { arrivalRate = Int passengers per minute
    , passengerQueue = List Pasenegers,
    , StationName = String
    , timeToNextStation = Int in minutes
    }

# A really short subway line
[{4/pm, [], "14th Street", 3min},{6/pm,[],"Union Station",4min}]

# Train arrival schedule (List Int)
arrivalTimes = [2,14,27,36...]
departedPassenegers = [] # List Passeneger
clock = 0
trainsEnroute = [] #(List (Int, Train)

# Basic main simulation loop outline
while (clock < 1440):
    if (clock = arrivalTimes[0]):
        arrivaltimes.pop(0)
        trainsEnroute.push(emptyTrain)
    for train in trainsEnroute:
        if train[0] in stations:
            decrementPassengerNumber(train)
            departedPassengers += disembark(train)
            if station != lastStation:
                embark(train, station)
            else:
                trainsEnroute.remove(train)
    for station in stations:
        addPassengers(station)
    clock++


#totalRideTime = 0
totalExposureTime = 0
for passenger in departedPassengers
    totalExposureTime += passenger.exposureTime
#    totalRideTime     += passenger.rideTime

print ( totalExposureTime ) # / totalRideTime )
    
def embark
def disembark
