# PMC-NetSim
A Network Simulation building tool, in python.  (Open source, free to use, for non-comercial use.)
Just download the full code and run it.  Add your own functions, easily, to interact with the data.
.
Designed to simulate Internet type networks with Packets of any type.
Normal user types and I.O.T. type users included. 
.
It’s easy.
The simulation will display details of the packets handled and the situations in the network. 
Add your own functions, easily, to interact with the data and extend the simulation in any way you wish.
.
The code shown here lists: 
How the classes are initially crated for, nodes, Lans and Packets
The setup code that controls all the settings and inputs for a simulation to run.
The actual simulator main code that uses the above parts needs to be downloaded from zaipaul.com
Or email zaipaul@yahoo.com stating what you will use the simulation code for.
.
This code allows any person, new to simulation building, to use and then adapt an internet type network simulator.
The more complex aditions to the code, does require a good understanding of coding in Python,
but anyone can add some code to control, analysis and view packets as they are moved through the network.
.
Detailed, basic help for adding your own code and data.
.
Simple adjustments to make to this simulator.
1.	Change the number and connectivity of the nodes in the network.
      View & edit the example node connection table in file : jnodes
2.	Change the Simulation settings via the python program : StartPMCNetSim
    worldClock = 0 # The simulation clock starts here.
    worldAttackTime = 2 # start attack at this time.
    worldAttackNode = 1 # preset the target.
    worldAttackLan = 1 # preset a Lan to be attacked via it’s list number.

    worldAttackThreshold = 80 # normal limit of packets arriving at Lans
    worldSendingThreshold = 500 # max - packets travelling towards a Lan

    displayData = False
    animate = False  # >>>>> Visual guide to network loaded - if created

    numberUsers = 100  # >>>>>  Set the number of users accessing network

    botnetPercentage = 80 # percentage of botnets (capacity)
    botnetNumber = (int(numberUsers / 100)) * botnetPercentage
    percentGoRouge = 80 # percent of IoT botnet that become rouge
    iot_rogue_percentage = percentGoRouge   #80 percent of the 80% IoT devices
    iot_rogue  = botnetNumber /100 * iot_rogue_percentage # number rouge

    maxSendPackets = 10 # Maximum packets sent per cycle by each device
    doCycles = 300  # >>>>>  Number of simulation cycles to run per test

    Matrixfilename = "jnodes.txt"  # holds the matrix of nodes and connections

    startFileNumber = 0 # The data files are expected to be numbered
    Datafilename = "Packets" #  + str(startFileNumber) + ".csv"



3.	Write your own functions.
        ownCode.py provides some readymade interfaces with NetSim to examine, change, control or update the system, including :
 
a) The Packets arrived at the Nodes.
b) Packets just received at the nodes from the Lans.
c) Packets being sent from nodes to their connected Lans.
d)  You can also access just the packets in transit, if you are no concerned 
        with what happens to a Packet as it moves through a node. 
.
  All of the demonstration functions are called from the : Your CODE HERE
    part of the main NetSim code.
            These provided functions, are automatically called via the function calls in
            NetSim.  Data used is passed to these functions and can be returned to NetSim.
             Write any code you wish here to access the list of : 
                  userDevices (Via their Lans) , Nodes and Packets.
           The easiest way to write your own function, is to add it to the python file : 
               ownCode.py
           Then add a function call from the NetSim section called : YourCODE HERE

           Follow the way the functions in OwnCode.py are called and passed data.

            Example function: nodeProcessing
            This function is passed 2 lists.
            The first list is all the packets in the simulation, travelling to their destination node.
            The other list is a link to all the nodes used in the simulation.
            def nodeProcessing(packetsToSend, nodes):
                    # write your own python code here ----------------------------- 

                     return nodes # returning the nodes list link, returns all changes made.

4.	 Use your own set of Packet data instead of the demo file provided.

   def getExcelDataset(): # IN THIS FILE READING FUNCTION
    
    if packetsReadIn > 99999: # Set number of packets per file

        if at_the_file > 0: # set to max number of files
            at_the_file = 0 # after all files used – goes back to file 0
        the_name = "Packets" + str(at_the_file) + ".csv"

files are expected in the form: Packets0.csv
But any changes can be made to the above code, for use of any data.

Then, just decide which or all of the attributes loaded, to use in your data set.
Here the same 5 items in each packet of data are copied into a list and returned.

packet_features = [
                list_convert[3],  # Proto (Protocol)
                list_convert[4],  # Saddr (Source Address)
                list_convert[6],  # Daddr (Destination Address)
                list_convert[8],  # Pkts (Total Packets)
                list_convert[10],  # State (Transaction State)
            ]

5.	Feel free to make any changes to the basic NetSim code to change the system as you wish. 
      a. Change the objects (Devices, Nodes and Packets) used in the simulation.
      b. Write your own code in the main simulation cycle to carry out any
         process you wish.
       c. Analysis and display or save the data in any way you wish.

Attribute the PMC-NetSim system as the basic simulator in your system.


