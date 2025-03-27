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
# Libraries may be needed at start of code.

# startPMCNewSim   =   NETSIM
# Basic starting code

# ------------------------------------------------------------------------------------------------------------
# >>>> Class userDivices creates any device on the LAN that sends or receives data as origination points.
class userDevice:  # >>>>> A workstation, laptop, tablet (IoT etc can use this code.)
    def __init__(self, diviceName, diviceNumber, ipAddress, macAddress, connect, maxPacketsHere,deviceType, attackNode,attackLAN):
        self.diviceName = diviceName
        self.diviceNumber = diviceNumber
        self.ipAddress = ipAddress # to store this IPAddress
        self.macAddress = macAddress # to store this Mac address
        self.connection = connect  # >>>>>  a node number connected to
        self.maxPackets = maxPacketsHere # sets maximum packets to send per cycle
        self.directConnections = 2  # # >>>>> 1-N computers on the LAN
        self.sendBalance = 0  # >>>>> All send WWW = 0
        self.packetsReceived = []  # >>>>> received from computers or nodes
        self.rogue_device = False # device has not been compromised if set to False
        self.count_sent_packets = 0
        self.options = ""
        self.deviceType = deviceType  #IoT OR OTHER Device
        self.attackNode = attackNode
        self.attackLAN = attackLAN

        self.warned = False
        self.attacked = False
        self.warned_message = ""

    def warning_ddos_status(self,warned_message):
        self.warned = True
        self.warned_message = warned_message

    def attacked_ddos_status(self):
        self.attacked = True

    def attack_Node(self, attackNode):
        self.attackNode = attackNode

    def attack_LAN(self, attackLAN):
        self.attackLAN = attackLAN

    def rogue_device_true(self):
        self.rogue_device = True #turn device to rogue

    def rogue_device_false(self):
        self.rogue_device = False #turn off rogue device

    def attack_target(self, options):
        self.options = options

    def change_send_balance(self,sendBalance): # if a server included
        if sendBalance >= 1:
            self.sendBalance = sendBalance  #the lower the number the higher rate for server

    def setMaxPackets(self, m):
        self.maxPackets = m

    def setConnections(self, cons):
        self.directConnections = cons  # >>>> set number of users to send to
        self.sendBalance = cons + 20  # >>>> control ratio going to server

    def changeLink(self, linkNumber):
        self.connection = linkNumber  # # >>>>>  the node it is connected to

    def sendPackets(self,sendNode):
        global maxSendPackets
        global users
        global worldClock
        global worldAttackTime
        global worldAttackNode
        global worldAttackLan

        
        if self.rogue_device == True and worldClock > worldAttackTime: # TIME FOR ATTACK
            sendNode = worldAttackNode ##### self.attackNode  #only happens when rogue
        
        self.count_sent_packets += 1
        newPackets = []
        # >>>>> # Application layer - select application sending data
        sendData = ""
        app = random.randint(0, 3)
        checksum = 0  # >>>>> denery data used as checksum here
        if app == 0:
            sendData = "13672, 234"  # >>>>> example data to be sent
            checksum = 10
        elif app == 1:
            sendData = "Excel 2,3,4,5,6"
            checksum = 15
        elif app == 2:
            sendData = "ACCOUNT "+str(random.randint(10, 300))
            checksum = sendData
        else:
            sendData = "Select Name from personal"  # >>>> Simulated SQL
            checksum = 24

        # >>>>> #Transport Layer - divide whole data into packets
        self.maxPackets = maxSendPackets # Set maximum packets to allowed normal limit - resets limit
        p = random.randint(1, self.maxPackets) # packets chosen this cycle
        rougePackets = self.maxPackets * 2 # extra packets sent by rough divice
        if self.count_sent_packets > 1 and self.rogue_device == True: # NOW device behaves rouge - 100 cycles starting
            p = rougePackets

        for i in range(p):  # # >>>>>  make p number packets
            aNode = random.randint(1,sendNode) # Randomly selects a node and then an IPAddress connected to that node - to send a packet
            toIPA = pickAUser(users,aNode)  # <<<< From list of users re: "111.111.222.333" 
            
            #>>>>>>> ROGUE packets would be described here <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            if self.rogue_device == True and worldClock > worldAttackTime:
                aNode = worldAttackNode
                toIPA = self.attackLAN

            np = packet(aNode, self.diviceNumber,self.macAddress,sendData, i, p, checksum, self.options,self.ipAddress,toIPA )  # # >>>>>  i packets per send
            newPackets.append(np)
        return newPackets #################################### <<<<<<<<<<<<<<<<<<<<<<< Node sends packets

    def factory_reset(self):
        self.maxPackets = 10
        self.sendBalance = 4
        self.rogue_device = False

    def receivePacket(self, packet):  # # >>>>>   packets received from other work stations/users or the server/s.
        self.packetsReceived.append(packet)

######################################## END user DEVICE ###################################################

