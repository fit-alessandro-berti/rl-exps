root = StrictPartialOrder(nodes=[
    Transition(label='Intake Review'),
    Transition(label='Preliminary Inspect'),
    Transition(label='Provenance Check'),
    Transition(label='Archival Research'),
    Transition(label='Material Testing'),
    Transition(label='Radiocarbon Date'),
    Transition(label='Stylistic Assess'),
    Transition(label='Expert Consult'),
    Transition(label='Findings Compile'),
    Transition(label='Internal Review'),
    Transition(label='Client Present'),
    Transition(label='Approval Confirm'),
    Transition(label='Secure Package'),
    Transition(label='Transport Arrange'),
    Transition(label='Chain Custody')
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