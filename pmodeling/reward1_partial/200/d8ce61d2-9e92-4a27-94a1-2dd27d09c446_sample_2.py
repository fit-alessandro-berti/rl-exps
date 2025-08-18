root = StrictPartialOrder(nodes=[
    Transition(label='Initial Audit'),
    Transition(label='Artist Review'),
    Transition(label='Material Check'),
    Transition(label='Condition Scan'),
    Transition(label='Ownership Verify'),
    Transition(label='Appraisal Update'),
    Transition(label='Restoration Plan'),
    Transition(label='Restoration Track'),
    Transition(label='Logistics Book'),
    Transition(label='Shipping Monitor'),
    Transition(label='Customs Clear'),
    Transition(label='Legal Compliance'),
    Transition(label='Ledger Update'),
    Transition(label='Exhibition Setup'),
    Transition(label='Public Showcase'),
    Transition(label='Archival Prep'),
    Transition(label='Final Report')
])

# Define the order of the nodes
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