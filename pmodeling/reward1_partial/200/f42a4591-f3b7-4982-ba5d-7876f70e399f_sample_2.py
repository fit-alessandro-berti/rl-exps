root = StrictPartialOrder(nodes=[
    Transition(label='Inspect Item'),
    Transition(label='Verify Provenance'),
    Transition(label='Document Condition'),
    Transition(label='Disassemble Parts'),
    Transition(label='Clean Components'),
    Transition(label='Analyze Damage'),
    Transition(label='Select Materials'),
    Transition(label='Perform Repairs'),
    Transition(label='Match Finishes'),
    Transition(label='Apply Treatments'),
    Transition(label='Reassemble Item'),
    Transition(label='Quality Check'),
    Transition(label='Photograph Results'),
    Transition(label='Update Archive'),
    Transition(label='Client Review'),
    Transition(label='Finalize Report')
])

# Define the dependencies
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