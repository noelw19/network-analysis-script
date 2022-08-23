# network-analysis-script
A script to capture packets going in and out of the network.

----------------------sniffer.py-----------------------------------------

Main thing to keep in mind, you must run sniffer program with sudo in order to sniff packets, otherwise error will occur and program will continue asking for an interface name.



----------------------pcapAnalyser.py------------------------------------

For the analyser to work:
    - copy the pcap file into the root dir of the py file.
    - when the analyser is run enter the name of the file into the first input prompt.

what the analyser does:
    
    The pcapAnalyser program takes a pcap file, and the reads it through the scapy library. When the file is initially read it prints some info on the pcap file, which is types of packets captured and how many of each type then it prints the total amount of packets that can be found in the file, for when you may need to enter a range to find packets within.

    Functionality:
        Option 1: 
            Allows the user to view all of the packets seperated in a pretty way with a copy of its index within the pcap file, for ability to look through the file.

            I done this by setting up a for loop that loops x to the total number of packets in the pcap file looking at each index and running the .show() method on the current index. A function called printPkt was set up to handle printing a packets in a pretty format, taking the pcap file and an index, which i used for all of the current options to print results. Reusable functions!.

        Option 2: 
            Allows the user to search through the pcap file and show all packets within a range, when the option is chosen the user is asked for a start index and an end index, the view in range function does some checking of the integers that are given to handle some simple errors that may occur such as:
                start and end being non-integers
                start being below 0
                end being greater than the total length of packets in the pcap file
                start integer being higher than end integer
            
            if the variable make it through then the variables are used in a for loop with range(start, end), and the printPkt function is run with the pcapfile aand the current instances index. printPkt(pcapfile, index)
        
        Option 3: 
            Allows a user to view a specific packet using the index which was simpler condering the printPkt function. Index is received via input, the input is checked to make sure it is a variable withing range, and then is passed to the printPkt function.


-------------------------Create pcap file ----------------------------

To create pcap file, you need to open wireshark and click capture, when you have captured enough, stop the capture and click file -> save as, (this doesnt matter but change file type from pcapng to pcap) and save into the py programs root directory.

