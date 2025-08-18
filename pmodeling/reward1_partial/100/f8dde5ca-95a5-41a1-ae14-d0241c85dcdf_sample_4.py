from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Material Scan'),
    Transition(label='Radiocarbon Test'),
    Transition(label='Style Compare'),
    Transition(label='Database Query'),
    Transition(label='Blockchain Prep'),
    Transition(label='Legal Review'),
    Transition(label='Ownership Audit'),
    Transition(label='Conservation Plan'),
    Transition(label='Expert Panel'),
    Transition(label='Report Draft'),
    Transition(label='Client Review'),
    Transition(label='Authority Submit'),
    Transition(label='Exhibit Setup'),
    Transition(label='Final Approval')
])

# Add the dependencies between the nodes
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

print(root)