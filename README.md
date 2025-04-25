📊 JSON Bigraph Visualizer

This Python project generates a bipartite graph (bigraph) from a collection of structured JSON objects. It identifies relationships between JSON entities and their properties, including shared properties across objects, and renders an interactive, visually appealing graph using D3.js in HTML.

🚀 Use Case

Designed for enterprise metadata analysis, this tool helps teams:
Visualize relationships between microservices or modules and their metadata attributes
Identify shared configuration properties across different services
Generate graph-based insights into architectural commonalities
For example, analyzing metadata from 10 microservices to show which services share the same database, runtime environment, or logging level.

```
**📁 Project Structure**

json_bigraph_project/
│
├── data/
│   └── metadata_samples.json          # Input JSON array of objects
│
├── src/
│   ├── data_loader.py                 # JSON loader
│   ├── graph_builder.py               # Builds the bigraph
│   ├── graph_exporter.py              # Exports JSON and HTML
│   └── templates/
│       └── graph_template.html        # D3.js graph template
│
├── output/
│   ├── bigraph.json                   # Graph data for visualization
│   └── bigraph.html                   # Final HTML visualization
│
├── run.py                             # Main entry point
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```
💠 Installation Instructions

1. Clone the repository
```
git clone git@github.com:srivatssan/visualizing-Graph-poc.git
cd visualizing-Graph-poc
```
2. Set up Python environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Run the application
```
python run.py
```
Output:

output/bigraph.json — Graph data
output/bigraph.html — Interactive HTML visualization

🌐** Visualize the Graph**

Due to browser security restrictions, run a local server:
```
cd output
python -m http.server 8000
```
Then open in browser:
```
http://localhost:8000/bigraph.html
```
✅ Interactive, zoomable, draggable graph rendered using D3.js

📊 **Features**

💡 Extracts relationships from any consistent JSON schema
⟳ Shows shared properties as edges across multiple objects
📊 Generates network graph using networkx
🌐 Outputs HTML visual using D3.js
⚙️ Enterprise-ready modular Python architecture

📚** Example Metadata Input**
```
{
  "service_name": "auth",
  "runtime_env": "python",
  "database": "postgres",
  "logging_level": "debug"
}
```
🧹 **Customization**

Modify metadata_samples.json in /data to reflect your domain
Customize graph styles in src/templates/graph_template.html
Extend with more attributes (e.g., regions, SLA, version)

📦** Dependencies
**
networkx – Graph creation and export
jinja2 – HTML templating engine
D3.js – JavaScript visualization (v7)

**Install via:**
```
pip install -r requirements.txt
```
📌 Roadmap

👨‍💼 Maintainers

Srivatssan Srinivasan

**🛡️ License**

This project is proprietary and intended for internal enterprise use. Please contact the author for licensing options.

**📣 Citation / Credit**

Inspired by the need to understand metadata reuse across distributed systems and microservices in enterprise IT landscapes.

