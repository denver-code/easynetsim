import random
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
