from scapy.all import *

def main():
    # Sniff packets on a specific interface
    sniff(iface="eth0", filter="tcp port 80", prn=packet_handler)

def packet_handler(pkt):
    # Process the packet
    print(pkt.summary())
    # Do something with the packet, like extract information or modify it

if __name__ == "__main__":
    main()