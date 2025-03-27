# ZaiPaul PMCNetSim Nodes Beta V2 Update version on 1/3/2025
#
# Network simulation tool, open source code, by Paul Coker (c) zaipaul 2023, 2024, 2025
# Contact via: zaipaul.com

# Code for the main sections, for adapting, of the ZaiPaul NetSim system.
# The full version with all code options available for download by request.
# more details at : zaipaul.com

# Please request the whole system downloaded via an email to zaipaul@yahoo.com
# Please state your nead for a network simulator

# NetSim is a free to use, open source code for internet networks
# It has been used by researchers to investigate:
# Mitegation of attacks
# DDOS early detection
# re-directing traffic

# Training in network simulation and network related research is available via zaipaul.com
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# The code section below, sets up all the starting parameters and states which are accessed via
# global variables

# This can be used and manually changed as required or use a GUI to do the setup

# This function can be called from the settings in : startPMCNewSim
# Or these settings can be adjusted via a GUI for different test runs

# Alternatively, adjust the settings here before the simulation is called
#------------------------------------------------------------------------

def beginNetSim(d,MatrixFile,DataFile):
    # Global shared data
    global totalPackets
    global totalNodesHere
    global displayData
    global maxSendPackets
    global targetNode
    global percentGoRouge
    global the_name # first data file used
    global at_the_file # data file starts at file name 0
    
    global worldClock
    global worldAttackTime # start attack at this time
    global worldAttackNode # preset the target
    global worldAttackLan
    global worldAttackThreshold
    global worldSendingThreshold

    worldClock = d[0] # starts at 0 time
    worldAttackTime = d[1] # start attack at this time
    worldAttackNode = d[2] # preset the target
    worldAttackLan = d[3] # time into test run before attack starts

    targetNode = d[4] # used to ID the main node the LAN uses

    worldAttackThreshold = d[5] # a simple way to state when nodes are being overloaded. (Could be sent per node in the node object.)
    worldSendingThreshold = d[6] # a mesurement of when a network becomes too busy
    
    print("Settings saved")
    print("Simulation started")

    displayData = d[7] # False # display some data during simulation run
    animate = d[8] # False  # >>>>> Visual guide to network loaded - if created


    numberUsers = d[9] # 100  # >>>>>  users accessing network
    
    botnetPercentage = d[10] # 90 # percentage of botnets (capacity) in the system
    botnetNumber = d[11] # (int(numberUsers / 100)) * botnetPercentage - converted into a count
    
    precentGoRouge = d[12] # controls the percentage of botnets that go rouge
    iot_rogue_percentage = d[13] # percentGoRouge   #80 percent of the 20% IoT devices
    iot_rogue  = d[14] # botnetNumber /100 * iot_rogue_percentage

    maxSendPackets = d[15] # 10 # Maximum packets sent from each device/user per cycle
    doCycles = d[16] # 300  # >>>>>  Number of simulation cycles to run per test
    CyclesComplete = 0  # >>>>> count cycles completed

    ######targetNode = 1 # set here which node is being targetted by malware of any type - to attack a connected device/user - if required
    
    filename = MatrixFile # "jnodes.txt"  # holds the matrix of nodes (Example = # "testnetwork.txt")

    the_name = DataFile + str(at_the_file) + ".csv" # the FIRST_ csv data file to be used
    
    numberNodes, nodeMatrix = loadNodeMatrix(filename) # >>>> Loan number and node connections matrix
    totalNodesHere = numberNodes

    # ---------------------------------------------------------------------------------------
    #displaySettings(numberNodes, numberUsers, maxSendPackets, doCycles, filename) # displays settings made

    startSimulation(doCycles, numberUsers, numberNodes, nodeMatrix, animate, botnetNumber) # <<<<<<<< SIMULATION STARTS

    print("Simulation stopped - ", doCycles, " cycles completed")
    Z = input("PRESS ENTER TO CLEAR")


################################################################################################################
#############################################################################
