from src.data_loader import load_json_objects
from src.graph_builder import build_bigraph
from src.graph_exporter import export_graph_to_json, render_html

def main():
    json_path = "data/metadata_samples.json"
    graph_json_path = "output/bigraph.json"
    html_output_path = "output/bigraph.html"
    template_folder = "src/templates"

    json_objects = load_json_objects(json_path)
    G = build_bigraph(json_objects)
    export_graph_to_json(G, graph_json_path)
    render_html(html_output_path, graph_json_path, template_folder)
    print(f"HTML graph generated at {html_output_path}")

if __name__ == "__main__":
    main()
