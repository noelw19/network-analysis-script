import scapy.all as scapy
import os

def clear():
    os.system('clear')

def readFile(fileName):
    try:
        pcap = scapy.rdpcap(fileName)
        print(f'\n\n{"="*20} pcap read successfully!{"="*20}\n')
        print(f'\nPcap Info:\t\t\t{pcap}\nPcap length in frames:\t\t{len(pcap)}\n')
        return pcap
    except:
        print(f'\nError reading file')
        readFile(input("Enter pcap file path: "))

def printPkt(pcap, i):
    print(f"{'='*20} Start {'='*20}\n\nIndex: {i}\n")
    print(f"\n{pcap[i].show()}\n\n")
    print(f"{'='*20} End {'='*20}\n\n")

def viewAll(pcap):
    for i in range(len(pcap)):
        printPkt(pcap, i)

def viewInRange(pcap, start, end):
    # if start and end is int, if end is less than total pcap length, and start is less than end, and start is greater than or equal to 0
    if int(start) and int(end) and int(end) <= len(pcap) and int(start) < int(end) and int(start) >= 0:
        for i in range(int(start), int(end)):
            printPkt(pcap, i)
    else:
        print('start and finish need to be numbers.')

def rangeCollector(pcap):
    start = input("Enter integer as start index: ")
    if int(start):
        end = input("Enter integer as end index:")
        if int(end):
            viewInRange(pcap, start, end)
        else:
            print("Invalid end index try again.")
    else:
            print("Invalid start index try again.")
        
def singlePacketReader(pcap):
    pktToRead = input("\nEnter the index of the packet to read: ")
    if int(pktToRead) and int(pktToRead) >= 0 and int(pktToRead) < len(pcap):
        print("\n")
        printPkt(pcap, int(pktToRead))

def pickFunction(pcap):
    options = input('What do you want to do?\n\n\t1. View all packets.\n\t2. View packets in range.\n\t3. View packet by index.\n\t0. To exit\n\t(Type clear to clear console.)\n\nInput: ')
    if options == 'clear':
        clear()
    elif int(options) == 1:
        # view all packets
        print("View all")
        viewAll(pcap)
        
    elif int(options) == 2:
        # View in range
        print('View packets in range')
        rangeCollector(pcap)
    elif int(options) == 3:
        # View specific packet
        print('View specific')
        singlePacketReader(pcap)
    elif int(options) == 0:
        return False
    else: 
        print('Enter valid option!\nTry again.')
        pickFunction()
        

    

def main():
    filePath = input("Enter pcap file path: ")
    pcapFile = readFile(filePath)
    while True:
        state = pickFunction(pcapFile)
        if state == False:
            print('\nGoodbye!\n\n')
            return False

    

if __name__ == '__main__':
    # to clear deprecation warnings for blowfish and cat5 from console
    # in /scapy/layers/ipsec
    clear()
    main()

