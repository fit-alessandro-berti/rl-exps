root = StrictPartialOrder(nodes=[
    Transition(label='Data Ingest'),
    Transition(label='Status Check'),
    Transition(label='Forecast Update'),
    Transition(label='Risk Assess'),
    Transition(label='Scenario Sim'),
    Transition(label='Model Run'),
    Transition(label='Option Select'),
    Transition(label='Team Review'),
    Transition(label='Plan Approve'),
    Transition(label='Procure Adjust'),
    Transition(label='Route Replan'),
    Transition(label='Inventory Shift'),
    Transition(label='Execute Updates'),
    Transition(label='Monitor KPIs'),
    Transition(label='Feedback Loop')
])

# Define dependencies
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[3])
root.order.add_edge(root.nodes[3], root.nodes[4])
root.order.add_edge(root.nodes[4], root.nodes[5])
root.order.add_edge(root.nodes[5], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])