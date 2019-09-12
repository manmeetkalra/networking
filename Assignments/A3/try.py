from copy import deepcopy


# The routers and networks are connected as follows
# N1- R1 - N2 - R2 - N3 - R3 - N4 - R4 - N5 - R5 - N6 - R6 - N7

#Initializing the routers with the networks where each tuple represents an entry in the table and where the first column is the Destination network,
#second column is the next hop router and the third column is the number of hops

r1 = [ ['N1', 'R1', 1],['N2', 'R1', 1] ]
r2 = [ ['N2', 'R2', 1],['N3', 'R2', 1] ]
r3 = [ ['N3', 'R3', 1],['N4', 'R3', 1] ]
r4 = [ ['N4', 'R4', 1],['N5', 'R4', 1] ]
r5 = [ ['N5', 'R5', 1],['N6', 'R5', 1] ]
r6 = [ ['N6', 'R6', 1],['N7', 'R6', 1] ]


#The print_table function prints the conents of the table
def print_table(router):
    for i in router:
        print i
	print

#The print_tables fucntion calls the print_table function and it prints the table of the six routers we have
def print_tables():
    print 'Router 1 Table:'
    print_table(r1)

    print 'Router 2 Table:'
    print_table(r2)

    print 'Router 3 Table:'
    print_table(r3)

    print 'Router 4 Table:'
    print_table(r4)

    print 'Router 5 Table:'
    print_table(r5)

    print 'Router 6 Table:'
    print_table(r6)


#The update_table function takes three parameter and this function update the routing table of the router after receiving advertise from the neigbhor router as follows:
#Case1 : The route already exits in the table do nothing
#Case2 : If the new route has shorter distance than the existing route, add the new route and change the next hop router and add 1 to the number of hops
#Case3 : If the route does not exist in the table, add the route and change the next hop router and add 1 to the number of hops
def update_table(recrouter, sendrouter, sendroutername):
    for i in sendrouter:
        match = False
        for j in recrouter:
		    #The route already exits in the table do nothing
            if i[0] == j[0]:
                match = True
				#The new route has shorter distance than the existing route
                if i[2] < j[2]:
                    recrouter.remove(j)
                    x = deepcopy(i)
	            recrouter.append(x) #Add the new route to the table
                    recrouter[-1][1] = sendroutername #Change the next hop router
                    recrouter[-1][2] = recrouter[-1][2] + 1 #And add one(1) to the number of hops

		#If the route does not exist in the table
        if match == False:
            y = deepcopy(i)
            recrouter.append(y) #Add the route to the table
            recrouter[-1][1] = sendroutername #Change the next hop router
            recrouter[-1][2] = recrouter[-1][2] + 1  #And add one(1) to the number of hops


#The print_tables function is called which prints the initial entiries of the routers in their routing tables
print 'The initial Routing Tables are as follows'
print
print_tables()


#
#All the routers are sending there routing table to their neighbors and the updatetable function is called which makes changes as it sees fit and the print_tables function is also called
for i in range(1,5):

 print 'Round ' + str(i)
 print
 #Router R1 sends its routing table to router R2
 update_table(r2,r1,'R1')

 #Router R2 sends its routing table to router R1 and router R3
 update_table(r1,r2,'R2')
 update_table(r3,r2,'R2')

 #Router R3 sends its routing table to router R2 and router R4
 update_table(r2,r3,'R3')
 update_table(r4,r3,'R3')

 #Router R4 sends its routing table to router R3 and router R5
 update_table(r3,r4,'R4')
 update_table(r5,r4,'R4')

 #Router R5 sends its routing table to router R4 and router R6
 update_table(r4,r5,'R5')
 update_table(r6,r5,'R5')

 #Router R6 sends its routing table to router R5
 update_table(r5,r6,'R6')

 #The function prints the updated routing tables of all the 6 routers
 print_tables()
