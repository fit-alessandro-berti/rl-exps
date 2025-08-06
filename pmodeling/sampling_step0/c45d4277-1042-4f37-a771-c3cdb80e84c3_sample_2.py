root = StrictPartialOrder(nodes=[
    Transition(label='Trend Scan'),
    Transition(label='Opportunity Map'),
    Transition(label='Expert Gather'),
    Transition(label='Idea Sprint'),
    Transition(label='Proto Build'),
    Transition(label='User Feedback'),
    Transition(label='Risk Review'),
    Transition(label='IP Audit'),
    Transition(label='Pilot Launch'),
    Transition(label='Stakeholder Meet'),
    Transition(label='Resource Shift'),
    Transition(label='Scale Up'),
    Transition(label='Impact Assess'),
    Transition(label='Knowledge Share'),
    Transition(label='Monitor Trends')
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