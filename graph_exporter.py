import json
import os
from jinja2 import Environment, FileSystemLoader
from networkx.readwrite import json_graph

def export_graph_to_json(G, path):
    data = json_graph.node_link_data(G)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def render_html(output_html_path, graph_json_path, template_folder):
    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template("graph_template.html")

    rendered_html = template.render(graph_data_path=os.path.basename(graph_json_path))

    with open(output_html_path, "w") as f:
        f.write(rendered_html)
