from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Transition(label='Provenance Check'),
        Transition(label='Sample Collection'),
        Transition(label='Spectroscopy Test'),
        Transition(label='Carbon Dating'),
        Transition(label='Expert Review'),
        Transition(label='Legal Clearance'),
        Transition(label='Cultural Assessment'),
        Transition(label='Digital Scan'),
        Transition(label='Report Draft'),
        Transition(label='Stakeholder Meet'),
        Transition(label='Acquisition Vote'),
        Transition(label='Restoration Plan'),
        Transition(label='Condition Report'),
        Transition(label='Archival Entry'),
        Transition(label='Final Approval')
    ]
)

# Define the order of activities
root.order.add_edge(root.nodes[0], root.nodes[1])
root.order.add_edge(root.nodes[1], root.nodes[2])
root.order.add_edge(root.nodes[1], root.nodes[3])
root.order.add_edge(root.nodes[2], root.nodes[4])
root.order.add_edge(root.nodes[3], root.nodes[5])
root.order.add_edge(root.nodes[4], root.nodes[6])
root.order.add_edge(root.nodes[6], root.nodes[7])
root.order.add_edge(root.nodes[7], root.nodes[8])
root.order.add_edge(root.nodes[8], root.nodes[9])
root.order.add_edge(root.nodes[9], root.nodes[10])
root.order.add_edge(root.nodes[10], root.nodes[11])
root.order.add_edge(root.nodes[11], root.nodes[12])
root.order.add_edge(root.nodes[12], root.nodes[13])
root.order.add_edge(root.nodes[13], root.nodes[14])

# Return the root of the POWL model
return root