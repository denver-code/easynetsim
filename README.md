# Easy Network Simulator

A simple network simulator for testing ping and routing between nodes.

## Installation

To install this package, run:

```bash
pip install easynetsim
```

## Usage
```python
from easynetsim import load_network, ping

# Define the network configuration
network_data = {
    "nodes": [
        {"hostname": "node1", "ip": "192.168.1.1"},
        {"hostname": "node2", "ip": "192.168.1.2"},
        {"hostname": "node3", "ip": "192.168.1.3"},
    ],
    "links": [
        {"source": "node1", "destination": "node2", "latency": 20},
        {"source": "node2", "destination": "node3", "latency": 20},
    ],
}

# Load the network
load_network(network_data)

# Ping a node
result = ping("node1", "192.168.1.3")
print(result)
```