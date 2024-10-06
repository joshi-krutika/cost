from flask import Flask, render_template, request, jsonify
import networkx as nx
from networkx.algorithms import bipartite
import pulp

# # app = Flask(__name__)

# # nodes = [
# #     {'data': {'id': 'I1', 'group': 'ing', 'cost': 5}},
# #     {'data': {'id': 'I2', 'group': 'ing', 'cost': 1}},
# #     {'data': {'id': 'I3', 'group': 'ing', 'cost': 5}},
# #     {'data': {'id': 'I4', 'group': 'ing', 'cost': 3}},
# #     {'data': {'id': 'I5', 'group': 'ing', 'cost': 3}},
# #     {'data': {'id': 'I6', 'group': 'ing', 'cost': 1}},
# #     {'data': {'id': 'I7', 'group': 'ing', 'cost': 1}},
# #     {'data': {'id': 'I8', 'group': 'ing', 'cost': 5}},
# #     {'data': {'id': 'I9', 'group': 'ing', 'cost': 3}},
# #     {'data': {'id': 'B2', 'group': 'ben'}},
# #     {'data': {'id': 'B1', 'group': 'ben'}},
# #     {'data': {'id': 'B3', 'group': 'ben'}}
# # ]

# # edges = [
# #     {'data': {'id': 'edge1', 'source': 'I1', 'target': 'B1'}},
# #     {'data': {'id': 'edge2', 'source': 'I2', 'target': 'B2'}},
# #     {'data': {'id': 'edge3', 'source': 'I3', 'target': 'B3'}},
# #     {'data': {'id': 'edge4', 'source': 'I4', 'target': 'B1'}},
# #     {'data': {'id': 'edge5', 'source': 'I5', 'target': 'B2'}},
# #     {'data': {'id': 'edge6', 'source': 'I6', 'target': 'B3'}},
# #     {'data': {'id': 'edge7', 'source': 'I7', 'target': 'B1'}},
# #     {'data': {'id': 'edge8', 'source': 'I8', 'target': 'B2'}},
# #     {'data': {'id': 'edge9', 'source': 'I9', 'target': 'B3'}}
# # ]

# # G = nx.Graph()
# # for node in nodes:
# #     G.add_node(node['data']['id'], group=node['data']['group'], cost=node['data'].get('cost'))
# # for edge in edges:
# #     G.add_edge(edge['data']['source'], edge['data']['target'])

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/compute')
# # def compute():
# #     return render_template('compute.html')


# # @app.route('/subgraph', methods=['POST'])
# # def subgraph():
# #     benefits = request.json['benefits']

# #     results = {}
# #     total_cost = 0

# #     for benefit in benefits:
# #         sub_nodes = list(G.neighbors(benefit)) + [benefit]
# #         subgraph = G.subgraph(sub_nodes)
        
# #         ingredient_costs = {node: G.nodes[node]['cost'] for node in sub_nodes if G.nodes[node]['group'] == 'ing'}
# #         neighbor_nodes = list(ingredient_costs.keys())
# #         ing_cost = list(ingredient_costs.values())
        
# #         A_matrix = bipartite.biadjacency_matrix(subgraph, row_order=neighbor_nodes, column_order=[benefit]).toarray()

# #         selected_indices, selected_costs, benefit_cost = cost_optimizer(A_matrix, ing_cost)
# #         selected_neighbors = [neighbor_nodes[idx] for idx in selected_indices]
        
# #         results[benefit] = {
# #             'selected_neighbors': selected_neighbors,
# #             'costs': selected_costs,
# #             'total_cost': benefit_cost
# #         }

# #         total_cost += benefit_cost

# #     return jsonify({'results': results, 'total_cost': total_cost})


# # @app.route('/graph_elements', methods=['GET'])
# # def graph_elements():
# #     return jsonify({'nodes': nodes, 'edges': edges})

# # def cost_optimizer(matrix, costs):
# #     n, m = len(matrix), len(matrix[0])
    
# #     x = [pulp.LpVariable(f"x_{i}", cat=pulp.LpBinary) for i in range(n)]
    
# #     degrees = [sum(matrix[i]) for i in range(n)]
    
# #     prob = pulp.LpProblem("Cost_optimization", pulp.LpMinimize)
    
# #     large_constant = max(costs) + 1
# #     prob += pulp.lpSum(costs[i] * x[i] - degrees[i] / large_constant * x[i] for i in range(n))
    
# #     for j in range(m):
# #         prob += pulp.lpSum(matrix[i][j] * x[i] for i in range(n)) >= 1, f"Constraint_benefit_{j}"

# #     prob.solve()
# #     selected_rows = [i for i in range(n) if x[i].value() == 1]
    
# #     selected_costs = [costs[i] for i in selected_rows]
    
# #     total_cost = sum(selected_costs)    

# #     return selected_rows, selected_costs, total_cost

# # if __name__ == '__main__':
# #     app.run(debug=True)




# from flask import Flask, render_template, request, jsonify
# import networkx as nx
# from networkx.algorithms import bipartite
# import pulp

# app = Flask(__name__)

# nodes = [
#     {'data': {'id': 'I1', 'group': 'ing', 'cost': 5}},
#     {'data': {'id': 'I2', 'group': 'ing', 'cost': 1}},
#     {'data': {'id': 'I3', 'group': 'ing', 'cost': 5}},
#     {'data': {'id': 'I4', 'group': 'ing', 'cost': 3}},
#     {'data': {'id': 'I5', 'group': 'ing', 'cost': 3}},
#     {'data': {'id': 'I6', 'group': 'ing', 'cost': 1}},
#     {'data': {'id': 'I7', 'group': 'ing', 'cost': 1}},
#     {'data': {'id': 'I8', 'group': 'ing', 'cost': 5}},
#     {'data': {'id': 'I9', 'group': 'ing', 'cost': 3}},
#     {'data': {'id': 'B2', 'group': 'ben'}},
#     {'data': {'id': 'B1', 'group': 'ben'}},
#     {'data': {'id': 'B3', 'group': 'ben'}}
# ]

# edges = [
#     {'data': {'id': 'edge1', 'source': 'I1', 'target': 'B1'}},
#     {'data': {'id': 'edge2', 'source': 'I2', 'target': 'B2'}},
#     {'data': {'id': 'edge3', 'source': 'I3', 'target': 'B3'}},
#     {'data': {'id': 'edge4', 'source': 'I4', 'target': 'B1'}},
#     {'data': {'id': 'edge5', 'source': 'I5', 'target': 'B2'}},
#     {'data': {'id': 'edge6', 'source': 'I6', 'target': 'B3'}},
#     {'data': {'id': 'edge7', 'source': 'I7', 'target': 'B1'}},
#     {'data': {'id': 'edge8', 'source': 'I8', 'target': 'B2'}},
#     {'data': {'id': 'edge9', 'source': 'I9', 'target': 'B3'}}
# ]

# G = nx.Graph()
# for node in nodes:
#     G.add_node(node['data']['id'], group=node['data']['group'], cost=node['data'].get('cost'))
# for edge in edges:
#     G.add_edge(edge['data']['source'], edge['data']['target'])

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/compute')
# def compute():
#     return render_template('compute.html')

# @app.route('/subgraph', methods=['POST'])
# def subgraph():
#     benefits = request.json['benefits']

#     results = {}
#     total_cost = 0

#     for benefit in benefits:
#         sub_nodes = list(G.neighbors(benefit)) + [benefit]
#         subgraph = G.subgraph(sub_nodes)
        
#         ingredient_costs = {node: G.nodes[node]['cost'] for node in sub_nodes if G.nodes[node]['group'] == 'ing'}
#         neighbor_nodes = list(ingredient_costs.keys())
#         ing_cost = list(ingredient_costs.values())
        
#         A_matrix = bipartite.biadjacency_matrix(subgraph, row_order=neighbor_nodes, column_order=[benefit]).toarray()

#         selected_indices, selected_costs, benefit_cost = cost_optimizer(A_matrix, ing_cost)
#         selected_neighbors = [neighbor_nodes[idx] for idx in selected_indices]
        
#         results[benefit] = {
#             'selected_neighbors': selected_neighbors,
#             'costs': selected_costs,
#             'total_cost': benefit_cost
#         }

#         total_cost += benefit_cost

#     return jsonify({'results': results, 'total_cost': total_cost})

# @app.route('/graph_elements', methods=['GET'])
# def graph_elements():
#     return jsonify({'nodes': nodes, 'edges': edges})

# def cost_optimizer(matrix, costs):
#     n, m = len(matrix), len(matrix[0])
    
#     x = [pulp.LpVariable(f"x_{i}", cat=pulp.LpBinary) for i in range(n)]
    
#     degrees = [sum(matrix[i]) for i in range(n)]
    
#     prob = pulp.LpProblem("Cost_optimization", pulp.LpMinimize)
    
#     large_constant = max(costs) + 1
#     prob += pulp.lpSum(costs[i] * x[i] - degrees[i] / large_constant * x[i] for i in range(n))
    
#     for j in range(m):
#         prob += pulp.lpSum(matrix[i][j] * x[i] for i in range(n)) >= 1, f"Constraint_benefit_{j}"

#     prob.solve()
#     selected_rows = [i for i in range(n) if x[i].value() == 1]
    
#     selected_costs = [costs[i] for i in selected_rows]
    
#     total_cost = sum(selected_costs)    

#     return selected_rows, selected_costs, total_cost

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, jsonify, request
import networkx as nx

app = Flask(__name__)

# Sample nodes and edges
nodes = [
    {'data': {'id': 'I1', 'group': 'ing', 'cost': 5}},
    {'data': {'id': 'I2', 'group': 'ing', 'cost': 1}},
    {'data': {'id': 'I3', 'group': 'ing', 'cost': 5}},
    {'data': {'id': 'I4', 'group': 'ing', 'cost': 3}},
    {'data': {'id': 'I5', 'group': 'ing', 'cost': 3}},
    {'data': {'id': 'I6', 'group': 'ing', 'cost': 1}},
    {'data': {'id': 'I7', 'group': 'ing', 'cost': 1}},
    {'data': {'id': 'I8', 'group': 'ing', 'cost': 5}},
    {'data': {'id': 'I9', 'group': 'ing', 'cost': 3}},
    {'data': {'id': 'B2', 'group': 'ben'}},
    {'data': {'id': 'B1', 'group': 'ben'}},
    {'data': {'id': 'B3', 'group': 'ben'}}
]

edges = [
    {'data': {'id': 'edge1', 'source': 'I1', 'target': 'B1'}},
    {'data': {'id': 'edge2', 'source': 'I2', 'target': 'B2'}},
    {'data': {'id': 'edge3', 'source': 'I3', 'target': 'B3'}},
    {'data': {'id': 'edge4', 'source': 'I4', 'target': 'B1'}},
    {'data': {'id': 'edge5', 'source': 'I5', 'target': 'B2'}},
    {'data': {'id': 'edge6', 'source': 'I6', 'target': 'B3'}},
    {'data': {'id': 'edge7', 'source': 'I7', 'target': 'B1'}},
    {'data': {'id': 'edge8', 'source': 'I8', 'target': 'B2'}},
    {'data': {'id': 'edge9', 'source': 'I9', 'target': 'B3'}}
]

# Creating the graph
G = nx.Graph()
for node in nodes:
    G.add_node(node['data']['id'], group=node['data']['group'], cost=node['data'].get('cost'))
for edge in edges:
    G.add_edge(edge['data']['source'], edge['data']['target'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/benefits')
def benefits():
    # Filter nodes for those that belong to the 'ben' group
    benefit_nodes = [node['data'] for node in nodes if node['data']['group'] == 'ben']
    return jsonify(benefit_nodes)

@app.route('/compute')
def compute():
    return render_template('compute.html')

@app.route('/subgraph', methods=['POST'])
def subgraph():
    benefits = request.json['benefits']

    results = {}
    total_cost = 0

    for benefit in benefits:
        sub_nodes = list(G.neighbors(benefit)) + [benefit]
        subgraph = G.subgraph(sub_nodes)
        
        ingredient_costs = {node: G.nodes[node]['cost'] for node in sub_nodes if G.nodes[node]['group'] == 'ing'}
        neighbor_nodes = list(ingredient_costs.keys())
        ing_cost = list(ingredient_costs.values())
        
        A_matrix = bipartite.biadjacency_matrix(subgraph, row_order=neighbor_nodes, column_order=[benefit]).toarray()

        selected_indices, selected_costs, benefit_cost = cost_optimizer(A_matrix, ing_cost)
        selected_neighbors = [neighbor_nodes[idx] for idx in selected_indices]
        
        results[benefit] = {
            'selected_neighbors': selected_neighbors,
            'costs': selected_costs,
            'total_cost': benefit_cost
        }

        total_cost += benefit_cost

    return jsonify({'results': results, 'total_cost': total_cost})

@app.route('/graph_elements', methods=['GET'])
def graph_elements():
    return jsonify({'nodes': nodes, 'edges': edges})

def cost_optimizer(matrix, costs):
    n, m = len(matrix), len(matrix[0])
    
    x = [pulp.LpVariable(f"x_{i}", cat=pulp.LpBinary) for i in range(n)]
    
    degrees = [sum(matrix[i]) for i in range(n)]
    
    prob = pulp.LpProblem("Cost_optimization", pulp.LpMinimize)
    
    large_constant = max(costs) + 1
    prob += pulp.lpSum(costs[i] * x[i] - degrees[i] / large_constant * x[i] for i in range(n))
    
    for j in range(m):
        prob += pulp.lpSum(matrix[i][j] * x[i] for i in range(n)) >= 1, f"Constraint_benefit_{j}"

    prob.solve()
    selected_rows = [i for i in range(n) if x[i].value() == 1]
    
    selected_costs = [costs[i] for i in selected_rows]
    
    total_cost = sum(selected_costs)    

    return selected_rows, selected_costs, total_cost

if __name__ == '__main__':
    app.run(debug=True)
