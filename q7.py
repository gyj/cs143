from mininet.topo import Topo, Node
from mininet.net import Mininet
from mininet.util import quietRun
from mininet.cli import CLI
from mininet.log import lg
from mininet.node import Controller, RemoteController
import pdb
import os
import time

"""

  To run this script: sudo python q7.py

"""

class MyTopo( Topo ):
    def __init__( self, enable_all = True ):
        # Add default members to class.
        super( MyTopo, self ).__init__()

        # Add nodes

        # example: self.add_node( <client's node ID>, Node(is_switch = ...), name=" ... ")

        YOUR CODE here



        # Add edges

        # example: to add a link with 20ms delay between host1 and host2
        #
        # self.add_edge( host1NodeId, host2NodeId, delay=20)
        #

        YOUR CODE here



        # Consider all switches and hosts 'on'
        self.enable_all()
        pass
    pass


def main():
    # instantiate the topology and mininet network and start the
    # network

    YOUR CODE here


    # obtain references to the host objects by using the network's
    # "idToNode" table with the host ID in the topoloy

    YOUR CODE here



    # call the "cmd()" API on host objects, e.g.,
    #
    # host1.cmd("ls -l")
    #
    # this API returns the executed's command output as a string

    
    # start polipo on the proxy and lighttpd on the server

    YOUR CODE HERE


    # the client fetches the bigfile

    YOUR CODE HERE


    # stop the network


    return

if __name__ == '__main__':
    # change info to debug for more verbose logging
    lg.setLogLevel( 'info')
    main()
    pass
