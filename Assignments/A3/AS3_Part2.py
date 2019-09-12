from copy import deepcopy


# The routers and  networks are connected as follows
# N1- R1 - N2 - R2 - N3 - R3 - N4 - R4 - N5 - R5 - N6 - R6 - N7 - R7 - N8

# Intialize the routers with Ni and Ni+1
# First entry - Destination Network
# Second entry - Next hop router
# Third entry - Number of Hops

routingTable_of_R1 = [ ['N1', 'R1', 1],['N2', 'R1', 1] ]
routingTable_of_R2 = [ ['N2', 'R2', 1],['N3', 'R2', 1] ]
routingTable_of_R3 = [ ['N3', 'R3', 1],['N4', 'R3', 1] ]
routingTable_of_R4 = [ ['N4', 'R4', 1],['N5', 'R4', 1] ]
routingTable_of_R5 = [ ['N5', 'R5', 1],['N6', 'R5', 1] ]
routingTable_of_R6 = [ ['N6', 'R6', 1],['N7', 'R6', 1] ]
routingTable_of_R7 = [ ['N7', 'R7', 1],['N8', 'R7', 1] ]


#The print_table function prints the contents of the table
def print_table(router):
    for j in router:
        print j


#The print_tables function calls the print_table function and it prints the table of the seven routers
def print_tables():
    print '\nRouter 1 Table:'
    print_table(routingTable_of_R1)

    print '\nRouter 2 Table:'
    print_table(routingTable_of_R2)

    print '\nRouter 3 Table:'
    print_table(routingTable_of_R3)

    print '\nRouter 4 Table:'
    print_table(routingTable_of_R4)

    print '\nRouter 5 Table:'
    print_table(routingTable_of_R5)

    print '\nRouter 6 Table:'
    print_table(routingTable_of_R6)

    print '\nRouter 7 Table:'
    print_table(routingTable_of_R7)


#The update_table function updates the routing table of the router after receiving routing tables from the neighbouring routers
def update_table(receiving_router, sending_router, sending_routername):
    for i in sending_router:
        match = 0
        for j in receiving_router:
            # Route already exists in the table
            if i[0] == j[0]:
                match = 1
				#The new route has shorter distance than the existing route
                if i[2] < j[2]:
                    receiving_router.remove(j)
                    x = deepcopy(i)
		    receiving_router.append(x) #Add the new route to the table
                    receiving_router[-1][1] = sending_routername #Change the next hop router
                    receiving_router[-1][2] = receiving_router[-1][2] + 1 # Add 1 to the number of hops

		#If the route does not exist in the table
        if match == 0:
            y = deepcopy(i)
            receiving_router.append(y) #Add the route to the table
            receiving_router[-1][1] = sending_routername #Change the next hop router
            receiving_router[-1][2] = receiving_router[-1][2] + 1  # Add 1 to the number of hops



print 'Initial Routing Tables of all the Routers'
print
print_tables()


for i in range(1,7):

 print '\n\n*****Round ' + str(i) + '*****'
 print
 #Router R1 sends its routing table to router R2
 update_table(routingTable_of_R2,routingTable_of_R1,'R1')

 #Router R2 sends its routing table to router R1 and router R3
 update_table(routingTable_of_R1,routingTable_of_R2,'R2')
 update_table(routingTable_of_R3,routingTable_of_R2,'R2')

 #Router R3 sends its routing table to router R2 and router R4
 update_table(routingTable_of_R2,routingTable_of_R3,'R3')
 update_table(routingTable_of_R4,routingTable_of_R3,'R3')

 #Router R4 sends its routing table to router R3 and router R5
 update_table(routingTable_of_R3,routingTable_of_R4,'R4')
 update_table(routingTable_of_R5,routingTable_of_R4,'R4')

 #Router R5 sends its routing table to router R4 and router R6
 update_table(routingTable_of_R4,routingTable_of_R5,'R5')
 update_table(routingTable_of_R6,routingTable_of_R5,'R5')

 #Router R6 sends its routing table to router R5 and R7
 update_table(routingTable_of_R5,routingTable_of_R6,'R6')
 update_table(routingTable_of_R7,routingTable_of_R6,'R6')

 #Router R7 sends its routing table to router R6
 update_table(routingTable_of_R6,routingTable_of_R7,'R7')

 #The function prints the updated routing tables of all the 7 routers
 print_tables()
