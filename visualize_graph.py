import sys
import json
import networkx as nx

def get_json_data(filename):
    with open(filename, 'r') as inf:
        data = json.load(inf)
        return data

def main():
    if len(sys.argv) != 2:
        print("Usage : python visualize_graph.py <model.json>")
    filename = sys.argv[1]
    json_data = get_json_data(filename)

if __name__ == '__main__':
    main()
