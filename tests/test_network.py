from easynetsim import load_network, ping


def test_ping():
    network_data = {
        "nodes": [
            {"hostname": "node1", "ip": "192.168.1.1"},
            {"hostname": "node2", "ip": "192.168.1.2"},
            {"hostname": "node3", "ip": "192.168.1.3"},
        ],
        "links": [
            {"source": "node1", "destination": "node2", "latency": 20},
        ],
    }
    load_network(network_data)
    result = ping("node1", "192.168.1.3")
    assert result["message"] == "No route to destination"
