import scapy.all as scapy
from scapy.layers import http

def sniffing(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if(packet.haslayer(http.HTTPRequest)):
        # print(packet[http.HTTPRequest].Host)
        print(f"\n{'='*40} Packet Start {'='*40}\n")
        print(packet.summary() + '\n')
        print(packet.show())
        print(f"\n{'='*40} Packet End {'='*40}\n")
        

# interface name added as arguement e.g wlan0, eth0
sniffing("wlp3s0")

