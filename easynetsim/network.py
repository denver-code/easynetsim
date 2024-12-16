import random
import networkx as nx
from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class NetworkNode:
    """
    Represents a node in the network with its properties.
    """

    hostname: str
    ip: str
    type: str = "device"
    mac: str = field(
        default_factory=lambda: f"00:00:00:00:00:{random.randint(0, 255):02x}"
    )


@dataclass
class NetworkLink:
    """
    Represents a link between two nodes in the network.
    """

    source: str
    destination: str
    latency: float
    packet_loss: float = 0
    bandwidth: float = 100


class NetworkSimulator:
    """
    A simulator for network operations and configurations.
    """

    def __init__(self):
        """
        Initialize an empty network graph.
        """
        self._network = nx.Graph()

    def load_network(self, config: Dict) -> None:
        """
        Load the network from a configuration dictionary.

        :param config: A dictionary containing network configuration
        """
        # Add nodes
        for node_config in config.get("nodes", []):
            node = NetworkNode(
                hostname=node_config["hostname"],
                ip=node_config["ip"],
                type=node_config.get("type", "device"),
                mac=node_config.get(
                    "mac", f"00:00:00:00:00:{random.randint(0, 255):02x}"
                ),
            )
            self._network.add_node(
                node.hostname, ip=node.ip, type=node.type, mac=node.mac
            )

        # Add links
        for link_config in config.get("links", []):
            link = NetworkLink(
                source=link_config["source"],
                destination=link_config["destination"],
                latency=link_config["latency"],
                packet_loss=link_config.get("packet_loss", 0),
                bandwidth=link_config.get("bandwidth", 100),
            )
            self._network.add_edge(
                link.source,
                link.destination,
                latency=link.latency,
                packet_loss=link.packet_loss,
                bandwidth=link.bandwidth,
            )

    def ping(self, source: str, destination_ip: str) -> Dict:
        """
        Simulate a ping operation between two nodes.

        :param source: Hostname of the source node
        :param destination_ip: IP address of the destination node
        :return: Dictionary with ping results
        """
        # Validate source node
        if not self._network.has_node(source):
            return {"message": "Source node not found"}

        # Find destination node
        destination_node = self._find_node_by_ip(destination_ip)
        if not destination_node:
            return {"message": "Destination node not found"}

        # Traverse network path
        path = self._traverse_network(source, destination_ip)
        if not path:
            return {"message": "No route to destination"}

        # Calculate latency
        latency = self._calculate_path_latency(path)

        # Check for packet loss
        if self._check_packet_loss(path):
            return {"message": "PING failed due to packet loss"}

        # Resolve MAC addresses
        source_mac = self._resolve_mac(self._network.nodes[source]["ip"])
        destination_mac = self._resolve_mac(destination_ip)

        return {
            "message": "PING successful!",
            "source_ip": self._network.nodes[source]["ip"],
            "source_mac": source_mac,
            "destination_ip": destination_ip,
            "destination_mac": destination_mac,
            "latency": f"{latency} ms",
            "path": path,
        }

    def _find_node_by_ip(self, ip: str) -> Optional[str]:
        """
        Find a node in the network by its IP address.

        :param ip: IP address to search for
        :return: Hostname of the node or None
        """
        for node, data in self._network.nodes(data=True):
            if data.get("ip") == ip:
                return node
        return None

    def _traverse_network(
        self, source: str, destination_ip: str
    ) -> Optional[List[str]]:
        """
        Traverse the network to find a path between source and destination.

        :param source: Source hostname
        :param destination_ip: Destination IP
        :return: Path between nodes or None
        """
        destination_node = self._find_node_by_ip(destination_ip)
        if not destination_node:
            return None

        try:
            path = nx.shortest_path(self._network, source, destination_node)
            return path
        except nx.NetworkXNoPath:
            return None

    def _calculate_path_latency(self, path: List[str]) -> float:
        """
        Calculate total latency for a network path.

        :param path: List of nodes in the path
        :return: Total latency
        """
        return sum(self._network[u][v]["latency"] for u, v in zip(path[:-1], path[1:]))

    def _check_packet_loss(self, path: List[str]) -> bool:
        """
        Check if packet loss occurs along the path.

        :param path: List of nodes in the path
        :return: True if packet loss occurs, False otherwise
        """
        return any(
            random.random() < self._network[u][v].get("packet_loss", 0)
            for u, v in zip(path[:-1], path[1:])
        )

    def _resolve_mac(self, ip: str) -> str:
        """
        Resolve MAC address for a given IP.
        Note: This is a stub method. In a real implementation,
        this would interact with ARP or a MAC address resolution service.

        :param ip: IP address
        :return: MAC address
        """
        # Placeholder implementation
        return f"00:00:00:00:00:{random.randint(0, 255):02x}"

    def get_network(self) -> nx.DiGraph:
        """
        Get the network graph.

        :return: Network graph
        """
        return self._network

    def get_nodes(self) -> List[NetworkNode]:
        """
        Get all nodes in the network.

        :return: List of NetworkNode objects
        """
        return list(self._network.nodes(data=True))

    def get_links(self) -> List[NetworkLink]:
        """
        Get all links in the network.

        :return: List of NetworkLink objects
        """
        return list(self._network.edges(data=True))

    def get_node_by_ip(self, ip: str) -> Optional[NetworkNode]:
        """
        Get a node by its IP address.

        :param ip: IP address
        :return: NetworkNode object or None
        """
        return self._network.nodes.get(ip)

    def get_node_by_hostname(self, hostname: str) -> Optional[NetworkNode]:
        """
        Get a node by its hostname.

        :param hostname: Hostname
        :return: NetworkNode object or None
        """
        return self._network.nodes.get(hostname)

    def get_link_by_nodes(self, source: str, destination: str) -> Optional[NetworkLink]:
        """
        Get a link by its source and destination nodes.

        :param source: Source node
        :param destination: Destination node
        :return: NetworkLink object or None
        """
        return self._network.get_edge_data(source, destination)

    def get_link_by_ip(
        self, source_ip: str, destination_ip: str
    ) -> Optional[NetworkLink]:
        """
        Get a link by its source and destination IP addresses.

        :param source_ip: Source IP
        :param destination_ip: Destination IP
        :return: NetworkLink object or None
        """

        return self._network.get_edge_data(source_ip, destination_ip)

    def get_link_by_hostname(
        self, source_hostname: str, destination_hostname: str
    ) -> Optional[NetworkLink]:
        """
        Get a link by its source and destination hostnames.

        :param source_hostname: Source hostname
        :param destination_hostname: Destination hostname
        :return: NetworkLink object or None
        """
        return self._network.get_edge_data(source_hostname, destination_hostname)

    def get_link_by_mac(
        self, source_mac: str, destination_mac: str
    ) -> Optional[NetworkLink]:
        """
        Get a link by its source and destination MAC addresses.

        :param source_mac: Source MAC
        :param destination_mac: Destination MAC
        :return: NetworkLink object or None
        """

        return self._network.get_edge_data(source_mac, destination_mac)
