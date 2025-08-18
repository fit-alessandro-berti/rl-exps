root = StrictPartialOrder(nodes=[
    Transition(label='Intake Document'),
    Transition(label='Visual Inspect'),
    Transition(label='Imaging Scan'),
    Transition(label='Material Test'),
    Transition(label='Database Cross'),
    Transition(label='Provenance Check'),
    Transition(label='Expert Consult'),
    Transition(label='Carbon Dating'),
    Transition(label='Forensic Analyze'),
    Transition(label='Anomaly Review'),
    Transition(label='Risk Assess'),
    Transition(label='Report Draft'),
    Transition(label='Insurance Quote'),
    Transition(label='Storage Plan'),
    Transition(label='Final Approval')
])

root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[0], root.nodes[2])
root.order.add_edge(root.nodes[0], root.nodes[3])
root.order.add_edge(root.nodes[1], root.nodes[4])
root.order.add_edge(root.nodes[2], root.nodes[5])
root.order.add_edge(root.nodes[3], root.nodes[6])
root.order.add_edge(root.nodes[4], root.nodes[7])
root.order.add_edge(root.nodes[5], root.nodes[8])
root.order.add_edge(root.nodes[6], root.nodes[9])
root.order.add_edge(root.nodes[7], root.nodes[10])
root.order.add_edge(root.nodes[8], root.nodes[11])
root.order.add_edge(root.nodes[9], root.nodes[12])
root.order.add_edge(root.nodes[10], root.nodes[13])
root.order.add_edge(root.nodes[11], root.nodes[14])
root.order.add_edge(root.nodes[12], root.nodes[15])