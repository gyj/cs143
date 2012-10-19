from mininet.topo import Topo, Node

""" custom topology example 2: same as sample_topo.py,
but will set link characteristics

  h1 -- s2 -- s3 -- s4 -- h5  
        |           |
        |           |
        h6          h7

"""

class MyTopo(Topo):
  def __init__(self, enable_all = True):
    # add default members to class
    super(MyTopo, self).__init__()

    # set host and switch IDs
    h1 = 1
    s2 = 2
    s3 = 3
    s4 = 4
    h5 = 5
    h6 = 6
    h7 = 7

    # add nodes
    self.add_node(h1, Node(is_switch = False))
    self.add_node(s2, Node(is_switch = True))
    self.add_node(s3, Node(is_switch = True))
    self.add_node(s4, Node(is_switch = True))
    self.add_node(h5, Node(is_switch = False))
    self.add_node(h6, Node(is_switch = False))
    self.add_node(h7, Node(is_switch = False))

    # add edges
    self.add_edge(h1,s2)
    self.add_edge(s2,h6)
    self.add_edge(s2,s3,delay=30)
    self.add_edge(s3,s4,delay=20)
    self.add_edge(s4,h7)
    self.add_edge(s4,h5)

    # turn all switches and hosts 'on'
    self.enable_all()

topos = {'sample_topo2' : (lambda: MyTopo())}
