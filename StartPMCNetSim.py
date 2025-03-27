# ZaiPaul PMCNetSim Nodes Beta V2 Update version on 1/3/2025
#
# Network simulation tool, open source code, by Paul Coker (c) zaipaul 2023, 2024
# Contact via: zaipaul.com
# Copyright Free to use, adapt, extend or convert in any way required.
# For none-comercial use only.
#
# This simulation is designed to be developed into any form of node based network required.
# Extensions to the Node objects would be required to add/use SDN or other types of networks.
#
# The basic system provides objects for users, nodes and packets
#
# To make processing quick and easy, all transported packets are held in one list and changed as they are moved from Node to Node.
# Currently as a packet arrives at it's destination node it is transfered to an 'arrived' list.
# You can then work with the packets at the Node level or after they are sent to a connected Lan, via another list.
# New and re-directed packets can be held in each node (as apposed to one list of all) if required, via the node object. 
#
# This is designed as a basic starting point for someone new to network simulation building.
# Create other classes, functions etc. to use the packets, connect to the network nodes, or other, as you require.
#
##################################################################################################################################
# Libraries used at start

#startPMCNewSim   =   NETSIM
# Basic starting code

from NetSim import beginNetSim

def main():
    worldClock = 0
    worldAttackTime = 2 # start attack at this time
    worldAttackNode = 1 # preset the target
    worldAttackLan = 1

    targetNode = 1 # default for the node under attack / targetted etc.

    worldAttackThreshold = 80 # normal limit of packets arriving <<<<<<<<<<<<<<<<< Decide
    #------------------------
    worldSendingThreshold = 500 # max - normal expect packets <<<<<<<<<<<<<<<< Decide
    #--------------------------

    displayData = False
    animate = False  # >>>>> Visual guide to network loaded - if created

    numberUsers = 100  # >>>>>  users accessing network

    botnetPercentage = 80 # percentage of botnets (capacity)
    botnetNumber = (int(numberUsers / 100)) * botnetPercentage
    percentGoRouge = 80 # percent of IoT botnet that become rouge
    iot_rogue_percentage = percentGoRouge   #80 percent of the 80% IoT devices
    iot_rogue  = botnetNumber /100 * iot_rogue_percentage # number ctually rouge

    maxSendPackets = 10 # Maximum packets sent from each device/user per cycle
    doCycles = 300  # >>>>>  Number of simulation cycles to run per test

    Matrixfilename = "jnodes.txt"  # holds the matrix of nodes (Example = # "testnetwork.txt")

    startFileNumber = 0
    Datafilename = "Packets" #  + str(startFileNumber) + ".csv"

    #-------------------------------------------------------------
    # Copy settings to NetSim and start
    #-------------------------------------------------------------

    d = [] # data to start netsim

    d.append(worldClock) # 0
    d.append(worldAttackTime)# 1 = 2 # start attack at this time
    d.append(worldAttackNode)# 2 = 1 # preset the target
    d.append(worldAttackLan)# = 3 1

    d.append(targetNode)#4  = 1 # default for the node under attack / targetted etc.

    d.append(worldAttackThreshold)#5 = 80 # normal limit of packets arriving <<<<<<<<<<<<<<<<< Decide
    #------------------------
    d.append(worldSendingThreshold)#6 = 500 # max - normal expect packets <<<<<<<<<<<<<<<< Decide
    #--------------------------

    d.append(displayData)# 7 = False
    d.append(animate)# 8 = False  # >>>>> Visual guide to network loaded - if created

    d.append(numberUsers)# 9 = 100  # >>>>>  users accessing network

    d.append(botnetPercentage)# 10 = 80 # percentage of botnets (capacity)
    d.append(botnetNumber)# 11 = (int(numberUsers / 100)) * botnetPercentage
    d.append(percentGoRouge)# 12 = 80 # percent of IoT botnet that become rouge
    d.append(iot_rogue_percentage)# 13 = percentGoRouge   #80 percent of the 80% IoT devices
    d.append(iot_rogue)# 14 = botnetNumber /100 * iot_rogue_percentage # number ctually rouge

    d.append(maxSendPackets)# 15 = 10 # Maximum packets sent from each device/user per cycle
    d.append(doCycles) # 16 = 300)#  # >>>>>  Number of simulation cycles to run per test


    print("Beginning NetSim")
    print(d)
    print(Matrixfilename)
    print(Datafilename)

    #yyy = input("yyy")

    beginNetSim(d,Matrixfilename,Datafilename)
main()

         
