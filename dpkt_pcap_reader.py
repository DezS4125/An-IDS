import dpkt

counter = 0
ipcounter = 0
tcpcounter = 0
udpcounter = 0

filename = '/home/dezs/test.pcap'

# Open the PCAP file in binary mode for proper packet handling
with open(filename, 'rb') as f:
    for ts, pkt in dpkt.pcap.Reader(f):

        counter += 1
        eth = dpkt.ethernet.Ethernet(pkt)

        # Check for IP packet type using integer comparison
        if eth.type != dpkt.ethernet.ETH_TYPE_IP:
            continue

        ip = eth.data
        ipcounter += 1

        # Check for protocol using integer comparison
        if ip.p == dpkt.ip.IP_PROTO_TCP:
            tcpcounter += 1

        if ip.p == dpkt.ip.IP_PROTO_UDP:
            udpcounter += 1

print("Total number of packets in the pcap file:", counter)
print("Total number of ip packets:", ipcounter)
print("Total number of tcp packets:", tcpcounter)
print("Total number of udp packets:", udpcounter)