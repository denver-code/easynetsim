import networkx as nx


def resolve_mac(ip):
    """
    Resolve the MAC address of a node based on its IP.
    """
    for node, node_data in nx.DiGraph().nodes(data=True):
        if node_data.get("ip") == ip:
            return node_data.get("mac")
    return None


def traverse_network(network: nx.DiGraph, source: str, destination_ip: str):
    """
    Use DFS to find a path from source to destination IP.
    """
    visited = set()

    def dfs(current_node: str, path: list) -> list:
        if current_node in visited:
            return []

        visited.add(current_node)

        if network.nodes[current_node].get("ip") == destination_ip:
            return path + [current_node]

        for neighbor in network.neighbors(current_node):
            result_path = dfs(neighbor, path + [current_node])
            if result_path:
                return result_path

        return []

    return dfs(source, [])
