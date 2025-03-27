# ZaiPaul PMCNetSim Nodes Beta V2 Update version on 1/3/2025
#
# Network simulation tool, open source code, by Paul Coker (c) zaipaul 2023, 2024,2025
# Contact via: zaipaul.com
# Copyright Free to use, adapt, extend or convert in any way required.
# For none-comercial use only.
#
# To DOWNLOAD the complete system contact: zaipaul.com
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
# Some Libraries may be needed at start.

#startPMCNewSim   =   NETSIM
# Basic starting code




class node:
    def __init__(self, nodeName, nodeNumber, processPerSec, buffer):
        self.nodeName = nodeName  # >>>>> Actual job - printer etc.
        self.nodeNumber = nodeNumber  # >>>>> Unique reference number
        self.routingTo = []  # # >>>>>  nodes that can be directly reached
        self.nextStep = []  # # >>>>>  The next node for routing to destination
        self.processPerSec = processPerSec  # >>>>> expected processing time
        self.bufferSize = buffer  # >>>>> If buffer included
        self.buffer = []  # >>>>> packets store in buffer
        self.sockets = 1 # allows programming of sockets if required
        self.MBS = 10  # >>>>> # = 10,000,000 / 1500 per packet typically = 6600 packets/second
        self.connection = []  # # >>>>>  a node number connected to
        self.bandwidth = []  # # >>>>>  capacity
        self.packetsHeld = []  # # >>>>>  held at that time
        self.receivedPackets = []  # # >>>>>  packets ATdestination = <<<<<<<<<<< THIS NODE ARRIVED
        self.computersConnected = []  # >>>>> for interconnected nodes
        self.resend = 0  # # >>>>>  no resent = pass to device or server - via number
        self.options = "" #holds options to give packets e.g. over flooding etc

    # ----------------------------
    def attack_target(self, options):
        self.options = options #puts the word "controller" etc in the options

    def setSockets(self, number):  # >>>>> socket value change
        self.sockets = number

    def setSpeed(self, number):  # >>>>> speed value change
        self.MBS = number

    def addComputer(self, number):  # >>>>> Adds workstate/laptop/tablet etc. If need to store in node object.
        self.computersConnected.append(number)

    def addLink(self, linkNumber, size):  # >>>>> adds to node it's actual connections
        self.connection.append(linkNumber)
        self.bandwidth.append(size)

    def updateRouting(self, goingTo, nextStep):  # >>>>> update node routing - if you need internal map
        self.routingTo.append(goingTo)
        self.nextStep.append(nextStep)  # # >>>>>  where to go next (node) to reach destination

    def arrivedPackets(self):  # >>>>> collects packets sent to this node
        for i in range(len(self.packetsHeld)):
            if self.packetsHeld[i].destination == nodeNumber:  # packet arrived
                self.receivedPackets.append(self.packetsHeld[i])

    def sendPackets(self, nextLink):  # >>>>> send packets to nodes or other nodes
        thePackets = []
        for i in range(len(self.packetsHeld)):  # >>>>> send all packets held
            # print("DD: " , self.packetsHeld[i].destination)
            if self.packetsHeld[i].destination == nextLink:  # next found
                thePackets.append(self.packetsHeld[i])
                # print("Sending")
                # for i in range(len(thePackets)):
                #    print("R: ", thePackets[i].destination)
                # print("Returning from node  = ", len(thePackets))
        return thePackets

    def serverReplys(self):  # >>>>> server node replies to message/request received
        thePackets = []
        for i in range(len(self.packetsHeld)):
            # print("RRR: " , self.packetsHeld[i].destination)
            if self.packetsHeld[i].destination == self.nodeNumber:  # # >>>>>  reply now
                thePackets.append(self.packetsHeld[i])

                # print("Returning from server = ", len(thePackets))
        return thePackets

    def transRouter(self):  # >>>>> # Transfer packets in server with IPAddress to router
        thePackets = []
        for i in range(len(self.packetsHeld)):
            if self.packetsHeld[i].IPAddress != "":  # # >>>>>  reply now
                thePackets.append(self.packetsHeld[i])
                # print("Sending router from server = ", len(thePackets))
        return thePackets

    # -------------------------------------------------
    def clearPackets(self):  # >>>>> # clear from list when all sent and not required
        self.packetsHeld = []

    def recievedPackets(self, packet):  # >>>>> add packets to held - if required
        self.packetsHeld.append(packet)

    def resetResent(self, node):
        self.resend = node  # >>>>>  pass all data to this node to re-direct

    def passToDevices(self): # If you need a centre server or data storage node
        serverPackets = []
        if self.resend == 0:  # # >>>>>  NOT pass to another node - these packets
            for i in range(len(self.packetsHeld)):
                if self.packetsHeld[i].sentFrom < 100:  # # >>>>> means from a device/node for a server
                    serverPackets.append(self.packetsHeld[i])  # # >>>>> node packets to be sent to a server
        self.packetsHeld = serverPackets  # packets selected and held before sending to server

#################################### END node class ##################################################

