# Easy Network Simulator

A simple network simulator for testing ping and routing between nodes.

## Installation

To install this package, run:

```bash
pip install easynetsim
```

## Usage
```python
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
result = simulator.ping("client1", "192.168.1.10")
print(result)
```

### Examples
More examples located in `examples` folder.

## Roadmap  
- [ ] Test cases
- [ ] Action for release autopublish