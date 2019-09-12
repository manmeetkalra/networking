from copy import deepcopy

print 'Assign3 Q2 - Umesh Dinkar'
print

# Assuming routers are connected as follows:
# r1---r2---r3---r4---r5---r6

# Initializing routers with Ni and Ni+1 i.e. two rows as
# Col 1: Destination Network
# Col 2: Next Hop Router
# Col 3: Number of Hops

print 'Each tuple represents an entry in the routing table!'
print 'First entry is the destination network, second entry is the next hop router and third entry is the number of hops!'
print

r1 = [
    ['N1', 'R1', 1],
    ['N2', 'R1', 1]
]

r2 = [
    ['N2', 'R2', 1],
    ['N3', 'R2', 1]
]

r3 = [
    ['N3', 'R3', 1],
    ['N4', 'R3', 1]
]

r4 = [
    ['N4', 'R4', 1],
    ['N5', 'R4', 1]
]

r5 = [
    ['N5', 'R5', 1],
    ['N6', 'R5', 1]
]

r6 = [
    ['N6', 'R6', 1],
    ['N7', 'R6', 1]
]

def printTable(router):
    for i in router:
        print i
    print

def printTables():
    print 'Router 1 Table:'
    printTable(r1)
    print 'Router 2 Table:'
    printTable(r2)
    print 'Router 3 Table:'
    printTable(r3)
    print 'Router 4 Table:'
    printTable(r4)
    print 'Router 5 Table:'
    printTable(r5)
    print 'Router 6 Table:'
    printTable(r6)

def updateTable(recvRouter, sendRouter, sendRouterName): # This implementation does NOT represent RIP! It's simplified for the given problem!
    for i in sendRouter:
        match = False
        for j in recvRouter:
            if i[0] == j[0]: # If the network is already in the table
                match = True
                if i[2] < j[2]: # If the new route is better than the current one
                    recvRouter.remove(j)
                    temp1 = deepcopy(i)
                    recvRouter.append(temp1) # Add route to the table
                    recvRouter[-1][1] = sendRouterName # Change next hop router
                    recvRouter[-1][2] = recvRouter[-1][2] + 1 # Add +1 to # hops 
        if match == False: # If the network-route is not in the table
            temp2 = deepcopy(i)
            recvRouter.append(temp2) # Add route to the table
            recvRouter[-1][1] = sendRouterName # Change next hop router
            recvRouter[-1][2] = recvRouter[-1][2] + 1 # Add +1 to # hops

# Initial routing tables

print 'Initial Routing Tables'
print
printTables()

# Round 1

print 'Round 1'
print
updateTable(r2,r1, 'R1') # R1 send out its routing table

# Router 1 update (since N1 disconnects)

r1 = [
    ['N1', 'R1', 16],
    ['N2', 'R1', 1],
    ['N3', 'R2', 2]
]

updateTable(r1,r2, 'R2')
updateTable(r3,r2, 'R2')

updateTable(r2,r3, 'R3')
updateTable(r4,r3, 'R3')

updateTable(r3,r4, 'R4')
updateTable(r5,r4, 'R4')

updateTable(r4,r5, 'R5')
updateTable(r6,r5, 'R5')

updateTable(r5,r6, 'R6')

printTables()

# Simulating rest of the rounds

for i in range(2,6):

    print 'Round ' + str(i)
    print
    # R1 sends its routing table
    updateTable(r2,r1, 'R1')

    # R2 sends its routing table
    updateTable(r1,r2, 'R2')
    updateTable(r3,r2, 'R2')

    # R3 sends its routing table
    updateTable(r2,r3, 'R3')
    updateTable(r4,r3, 'R3')

    # R4 sends its routing table
    updateTable(r3,r4, 'R4')
    updateTable(r5,r4, 'R4')

    # R5 sends its routing table
    updateTable(r4,r5, 'R5')
    updateTable(r6,r5, 'R5')

    # R6 sends its routing table
    updateTable(r5,r6, 'R6')

    printTables()


print "INSTABILITY: As you can see, despite having no way to reach N1, the routers in the AS believe that they can reach N1."
print "It is because R1 thinks that it can reach N1 via R2 and R2 thinks that it can reach N1 via R1, which is a loop."
print "Reverse poisoning can be used to solve the issue."
