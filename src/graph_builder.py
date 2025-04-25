import networkx as nx

def build_bigraph(json_objects):
    G = nx.Graph()

    for obj in json_objects:
        service = obj["service_name"]
        G.add_node(service, type="service")

        for key, value in obj.items():
            if key == "service_name":
                continue
            node_id = f"{key}:{value}"
            G.add_node(node_id, type="property", label=key)
            G.add_edge(service, node_id)

    return G
