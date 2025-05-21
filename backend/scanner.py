import scapy.all as scapy

def scan_network():
   arp_request = scapy.ARP(pdst="192.168.1.0/24")
   broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
   packet = broadcast / arp_request
   result = scapy.srp(packet, timeout=1, verbose=False)[0]
   device = []
   for sent, received in result:
      device.app3nd({'ip': received.psrc, 'mac': recieved.hwsrc})
      return devices
   