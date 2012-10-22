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

    follow instructions embedded in-line
 
"""

class MyTopo( Topo ):
  def __init__( self, enable_all = True ):
    # [TODO] paste your code from topo1.py

    # enable all switches and hosts
    self.enable_all()
    pass
  pass


def main():
    # instantiate topology and mininet network and start 
    # the network
    # [TODO] your code here


    # obtain references to host objects by using network's
    # "idToNode" table with the host ID in the topoloy
    # see net.py for details
    # [TODO] your code here


    # call "cmd()" API on host objects, e.g., h7.cmd("ls -l")
    # the API returns the executed command output as string
    
    # start lighttpd on web server and polipo on proxy
    # [TODO] your code here


    # client gets file10M through: 1) web server and 2) proxy
    # run multiple times, do time measurements, handle empirical data
    # [TODO] your code here


    # stop the network
    # [TODO] your code here


    return

if __name__ == '__main__':
    # change info to debug for more verbose logging
    lg.setLogLevel( 'info')
    main()
    pass
