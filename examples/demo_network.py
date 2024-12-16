from easynetsim import NetworkSimulator

# Define network configuration
config = {
    "nodes": [
        {"hostname": "router1", "ip": "192.168.1.1", "type": "router"},
        {"hostname": "server1", "ip": "192.168.1.10", "type": "server"},
        {"hostname": "client1", "ip": "192.168.1.100", "type": "client"},
    ],
    "links": [
        {
            "source": "router1",
            "destination": "server1",
            "latency": 10,
            "packet_loss": 0.05,
        },
        {
            "source": "router1",
            "destination": "client1",
            "latency": 20,
            "packet_loss": 0.01,
        },
    ],
}

# Initialize network simulator
simulator = NetworkSimulator()
simulator.load_network(config)

# Demonstrate ping operation
print("Pinging from client1 to server1:")
result = simulator.ping("client1", "192.168.1.10")
print(result)

# Demonstrate network information retrieval
print("\nNetwork Nodes:")
for node in simulator.get_nodes():
    print(f"Hostname: {node[0]}, IP: {node[1]['ip']}, Type: {node[1]['type']}")

print("\nNetwork Links:")
for link in simulator.get_links():
    print(f"From: {link[0]}, To: {link[1]}, Latency: {link[2]['latency']} ms")


"""
Output:

Pinging from client1 to server1:
{'message': 'PING successful!', 'source_ip': '192.168.1.100', 'source_mac': '00:00:00:00:00:48', 'destination_ip': '192.168.1.10', 'destination_mac': '00:00:00:00:00:f4', 'latency': '30 ms', 'path': ['client1', 'router1', 'server1']}

Network Nodes:
Hostname: router1, IP: 192.168.1.1, Type: router
Hostname: server1, IP: 192.168.1.10, Type: server
Hostname: client1, IP: 192.168.1.100, Type: client

Network Links:
From: router1, To: server1, Latency: 10 ms
From: router1, To: client1, Latency: 20 ms
"""
