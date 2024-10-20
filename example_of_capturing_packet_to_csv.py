import scapy.all as scapy

# Configure capture interface and filter
iface = "wlp0s20f3"  # Replace with your network interface
filter = "tcp or udp"  # Adjust filter as needed

# Start capturing packets
packets = scapy.sniff(iface=iface, filter=filter, count=1)  # Adjust count as needed

import pandas as pd
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP, UDP

def extract_features(packet):
    features = {}
    
    # Flow-based features
    features['Source IP'] = packet[IP].src
    features['Destination IP'] = packet[IP].dst
    features['Source Port'] = packet[TCP].sport if TCP in packet else packet[UDP].sport
    features['Destination Port'] = packet[TCP].dport if TCP in packet else packet[UDP].dport
    features['Protocol'] = packet[IP].proto
    features['Flow Duration'] = packet.time - packet[Ether].time
    features['Total Fwd Bytes'] = packet[IP].len
    features['Total Bwd Bytes'] = packet[IP].len
    features['Total Fwd Packets'] = 1
    features['Total Bwd Packets'] = 1
    # Add more features as needed
    
    return features

# Create a DataFrame to store extracted features
data = []

for packet in packets:
    features = extract_features(packet)
    data.append(features)

df = pd.DataFrame(data)

print(df)