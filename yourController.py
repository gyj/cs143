from pox.core import core
import pox.openflow.libopenflow_01 as of

"""

This is a simple OpenFlow controller. It acts as a hub or can be 
made a simple learning switch.

For our purpose, only one controller should suffice. Hence, you 
may need to use 'self.connection.dpid' to select a switch.

Straw man design of this code is based on tutorial code available 
from https://github.com/noxrepo/pox 

"""

log = core.getLogger()

class yourController (object):
  """
  yourController object is created for each switch that connects.
  connection object for the switch is passed to __init__ function.
  """
  def __init__ (self, connection):
    # keep track of the connection to the switch so that we can
    # send messages to the switch
    self.connection = connection

    # bind PacketIn event listener
    connection.addListeners(self)

    # map from a mac addr instance to the corresponding output
    # port number to use to reach that mac addr
    # use this table to keep track of which ethernet address is on
    # which switch port (keys are MACs, values are ports)
    self.mac_to_port = {}


  def send_packet (self, buffer_id, raw_data, out_port, in_port):
    """
    sends a packet out of the specified switch port.
    if buffer_id is a valid buffer on the switch, use it.
    otherwise, send the raw data in raw_data.
    'in_port' is the port number that packet arrived on.  
    use OFPP_NONE if you're generating this packet.
    """
    msg = of.ofp_packet_out()
    msg.in_port = in_port
    if buffer_id != -1 and buffer_id is not None:
      # We got a buffer ID from the switch; use that
      msg.buffer_id = buffer_id
    else:
      # No buffer ID from switch -- we got the raw data
      if raw_data is None:
        # No raw_data specified -- nothing to send!
        return
      msg.data = raw_data

    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    # Send message to switch
    self.connection.send(msg)


  def act_like_hub (self, packet, packet_in):
    """
    Implement hub-like behavior -- send all packets to all ports besides
    the input port.
    """

    # want to output to all ports -- do it using the special OFPP_FLOOD port 
    # as the output port. could have also used OFPP_ALL.
    self.send_packet(packet_in.buffer_id, packet_in.data,
                     of.OFPP_FLOOD, packet_in.in_port)

    # if we didn't get a valid buffer_id, a slightly better implementation 
    # would check that we got the full data before sending it 
    # i.e., len(packet_in.data) should equal packet_in.total_len.


  def act_like_switch (self, packet, packet_in):
    """
    Implement switch-like behavior
    """

    """ [delete this line if you work on below]

    # here's some psuedocode to start you off implementing a learning
    # switch. you'll need to rewrite it as real Python code.

    # learn the port for the source MAC
    self.mac_to_port ... <add or update entry>

    if the port associated with the destination MAC of the packet is known:
      # send packet out the associated port
      self.send_packet(packet_in.buffer_id, packet_in.data,
                       ..., packet_in.in_port)

      # once you have the above working, try pushing a flow entry
      # instead of resending the packet (comment out the above and
      # uncomment and complete the below.)

      log.debug("Installing flow...")
      # maybe the log statement should have source/destination/port?

      #msg = of.ofp_flow_mod()
      #
      # set fields to match received packet
      #msg.match = of.ofp_match.from_packet(packet)
      #
      #< set other fields of flow_mod (timeouts? buffer_id?) >
      #
      #< add an output action, and send -- similar to send_packet() >

    else:
      # Flood the packet out everything but the input port
      # This part looks familiar, right?
      self.send_packet(packet_in.buffer_id, packet_in.data,
                       of.OFPP_FLOOD, packet_in.in_port)

    [delete this line after completing code above] """


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # this is parsed packet data
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # actual ofp_packet_in message

    # act_like_switch is commented out
    self.act_like_hub(packet, packet_in)
    #self.act_like_switch(packet, packet_in)


def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    yourController(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)

