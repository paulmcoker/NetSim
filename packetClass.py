# ZaiPaul PMCNetSim Nodes Beta V2 Update version on 1/3/2025
#
# Network simulation tool, open source code, by Paul Coker (c) zaipaul 2023, 2024, 2025
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
# Libraries may be needed at the start of code.

#startPMCNewSim   =   NETSIM
# Basic starting code


class packet:  # >>>>> structure of a packet with some methods ==================== Must know start node
    def __init__(self, destination, sentFrom, macAddress, data, part, maxParts, checksum, options,fromIPA,toIPA):
        self.destination = destination  # # >>>>>  NODE device number - destination <<<<<<<<<<<<<<<<<<<< SEND to NODE
        self.IPAddress = toIPA  # >>>> IPAddress of destination
        self.FromIPAddress = fromIPA  # >>>> This LAN IPAddress
        self.sentFrom = sentFrom  # NODE sent from <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FROM
        self.macAddress = macAddress
        self.part = part  # How many packet parts in message
        self.maxParts = maxParts
        self.acknowledgementNumber = 0  # 0 = not required
        self.checksum = checksum  # Denery check value sim real
        self.options = options  # Use to carry TEXT options
        self.data = data  # Actual Data to send
        self.protocol = "Protocol"
        self.node_start = random.randint(1,totalNodesHere)   #node_start selected
        self.atNode = self.node_start
        self.state = ""

    def addIPA(self, IPA):  # Change destination IPAddress
        self.IPAddress = IPA

    def fromIPA(self, IPA): # returns IPAddress
        self.FromIPAddress = IPA

    def change_options(self, modify):
        self.options = modify  # function for modification

    def moveNode(self, newNode): #Packet has moved to another node
        self.atNode = newNode

    def nodeNow(self):
        return self.atNode

    def giveExcelData(self, list_convert):
            self.protocol = list_convert[0],  # Proto (Protocol)
            self.FromIPAddress = list_convert[1],  # Saddr (Source Address)
            self.IPAddress = list_convert[2],  # Daddr (Destination Address)
            self.part = list_convert[3],  # Pkts (Total Packets)
            self.state = list_convert[4],  # State (Transaction State)
        
