import random
import networkx as nx
from .utils import resolve_mac, traverse_network

# Initialize the network graph
network = nx.DiGraph()


# Load network from configuration data
def load_network(config: dict):
    """
    Load the network from a configuration dictionary.
    """
    for node in config["nodes"]:
        network.add_node(
            node["hostname"],
            ip=node["ip"],
            type=node.get("type", "device"),
            mac=node.get("mac", f"00:00:00:00:00:{random.randint(0, 255):02x}"),
        )

    for link in config["links"]:
        network.add_edge(
            link["source"],
            link["destination"],
            latency=link["latency"],
            packet_loss=link.get("packet_loss", 0),
            bandwidth=link.get("bandwidth", 100),
        )


def ping(source: str, destination_ip: str):
    """
    Simulate a ping operation between two nodes.
    """
    if not network.has_node(source):
        return {"message": "Source node not found"}

    destination_node = None
    for node, data in network.nodes(data=True):
        if data.get("ip") == destination_ip:
            destination_node = node
            break

    if not destination_node:
        return {"message": "Destination node not found"}

    path = traverse_network(network, source, destination_ip)

    if not path:
        return {"message": "No route to destination"}

    latency = 0
    for u, v in zip(path[:-1], path[1:]):
        edge_data = network[u][v]
        latency += edge_data["latency"]

    if any(
        random.random() < network[u][v].get("packet_loss", 0)
        for u, v in zip(path[:-1], path[1:])
    ):
        return {"message": "PING failed due to packet loss"}

    source_mac = resolve_mac(network.nodes[source]["ip"])
    destination_mac = resolve_mac(destination_ip)

    return {
        "message": "PING successful!",
        "source_ip": network.nodes[source]["ip"],
        "source_mac": source_mac,
        "destination_ip": destination_ip,
        "destination_mac": destination_mac,
        "latency": f"{latency} ms",
        "path": path,
    }
