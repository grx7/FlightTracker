from db_commands import FlightTrackerCluster

myCluster = FlightTrackerCluster()
myCluster.changeKeySpace('plane')

quit = False

print ("\nAvailable queries: 'time', 'price', 'carrier', 'origin', 'destination', or 'departure_date'\n")
while quit == False:
    key = raw_input('Enter a key name (or type Q to quit): ')
    if key != 'Q':
        print '\n RESULTS: ' + str(myCluster.selectFromTable(key, 'Tickets')) + '\n'
    else:
        print "\nGoodbye!"
        quit = True