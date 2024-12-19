from easynetsim import NetworkSimulator

config = {
    "nodes": [
        {"hostname": "router1", "ip": "192.168.1.1", "type": "router"},
        {"hostname": "switch1", "ip": "", "type": "switch"},
        {"hostname": "pc1", "ip": "192.168.1.2", "type": "client"},
        {"hostname": "pc2", "ip": "192.168.1.3", "type": "client"},
        {"hostname": "pc3", "ip": "192.168.1.4", "type": "client"},
        {"hostname": "switch2", "ip": "", "type": "switch"},
        {"hostname": "pc4", "ip": "192.168.1.5", "type": "client"},
        {"hostname": "pc5", "ip": "192.168.1.6", "type": "client"},
        {"hostname": "pc6", "ip": "192.168.1.7", "type": "client"},
        {"hostname": "switch3", "ip": "", "type": "switch"},
        {"hostname": "pc7", "ip": "192.168.1.8", "type": "client"},
        {"hostname": "pc8", "ip": "192.168.1.9", "type": "client"},
        {"hostname": "pc9", "ip": "192.168.1.10", "type": "client"},
    ],
    "links": [
        {
            "source": "router1",
            "destination": "switch1",
            "latency": 10,
            "packet_loss": 0,
        },
        {
            "source": "router1",
            "destination": "switch2",
            "latency": 10,
            "packet_loss": 0,
        },
        {
            "source": "router1",
            "destination": "switch3",
            "latency": 10,
            "packet_loss": 0,
        },
        {
            "source": "switch1",
            "destination": "pc1",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch1",
            "destination": "pc2",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch1",
            "destination": "pc3",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch2",
            "destination": "pc4",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch2",
            "destination": "pc5",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch2",
            "destination": "pc6",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch3",
            "destination": "pc7",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch3",
            "destination": "pc8",
            "latency": 5,
            "packet_loss": 0,
        },
        {
            "source": "switch3",
            "destination": "pc9",
            "latency": 5,
            "packet_loss": 0,
        },
    ],
}

# Initialize network simulator
simulator = NetworkSimulator()
simulator.load_network(config)

result = simulator.ping("pc1", "192.168.1.10")
print(result)
