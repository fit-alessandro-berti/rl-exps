root = StrictPartialOrder(nodes=[
    Transition(label='Ingredient Sourcing'),
    Transition(label='Sample Testing'),
    Transition(label='Oil Extraction'),
    Transition(label='Blend Formulation'),
    Transition(label='Quality Control'),
    Transition(label='Aging Process'),
    Transition(label='Allergen Check'),
    Transition(label='Market Research'),
    Transition(label='Bottle Design'),
    Transition(label='Label Approval'),
    Transition(label='Packaging Setup'),
    Transition(label='Batch Mixing'),
    Transition(label='Scent Profiling'),
    Transition(label='Client Feedback'),
    Transition(label='Release Scheduling'),
    Transition(label='Regulatory Review'),
    Transition(label='Sales Training')
])

# Define the dependencies between the activities
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