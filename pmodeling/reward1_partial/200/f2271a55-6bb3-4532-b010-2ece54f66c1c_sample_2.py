root = StrictPartialOrder(nodes=[
    Transition(label='Provenance Check'),
    Transition(label='Spectroscopy Test'),
    Transition(label='Carbon Dating'),
    Transition(label='Style Analysis'),
    Transition(label='Image Scanning'),
    Transition(label='Restoration Scan'),
    Transition(label='Appraiser Review'),
    Transition(label='Database Match'),
    Transition(label='Blockchain Entry'),
    Transition(label='Certificate Issue'),
    Transition(label='Forgery Detect'),
    Transition(label='Report Compilation'),
    Transition(label='Client Briefing'),
    Transition(label='Secure Storage'),
    Transition(label='Final Approval')
])

# Define the order of the activities
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