root = StrictPartialOrder(nodes=[
    Transition(label='Data Aggregation'),
    Transition(label='Anomaly Detect'),
    Transition(label='Risk Assess'),
    Transition(label='Demand Model'),
    Transition(label='Stakeholder Sync'),
    Transition(label='Auto Negotiate'),
    Transition(label='Inventory Optimize'),
    Transition(label='Contingency Plan'),
    Transition(label='Resource Allocate'),
    Transition(label='Sustainability Check'),
    Transition(label='Compliance Verify'),
    Transition(label='Impact Score'),
    Transition(label='Distribution Plan'),
    Transition(label='Feedback Loop'),
    Transition(label='Performance Audit'),
    Transition(label='Schedule Execute')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
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
root.order.add_edge(root.nodes[14], root.nodes[15])
root.order.add_edge(root.nodes[15], root.nodes[16])