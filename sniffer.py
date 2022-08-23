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
        
def interfaceAcceptor():
    interface = input("Enter interface to take a whiff of: ")
    try: 
        sniffing(interface)
    except:
        print("Interface error.\nTry again.\n\n")
        interfaceAcceptor()

interfaceAcceptor()


# interface name added as arguement e.g wlan0, eth0



