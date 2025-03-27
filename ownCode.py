
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
#-----------------------------------------------------------------------------

############################# Your Own Code goes below ###############################


# If required, process packets in transit in the nodes and how nodes will use them

def nodeProcessing(packets_in_transit, nodes):
  # nodeProcessing(packetsToSend, nodes) - called as


    return nodes

#------------------------------------------------------------------------

# Send packets arrived at destination node - to Lan / URL

def sendLan(nodes, Lans): # pointers to the nodes and users list given


    return nodes

#------------------------------------------------------------------------

# Add code here as to what you want the Lans to do with the Data Packets

def actionLan(Lans):




    return Lans

#------------------------------------------------------------------------

# Graphical display of network, nodes and Lans - if you want to write your code

def displayGraphics(nodes, lans):






    return "OK"

#---------------------------------------------------------------------
