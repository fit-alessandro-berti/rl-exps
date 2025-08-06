root = StrictPartialOrder(nodes=[
    Transition(label='Scenario Setup'),
    Transition(label='Resource Mapping'),
    Transition(label='Team Briefing'),
    Transition(label='Tech Deployment'),
    Transition(label='Data Sync'),
    Transition(label='Comm Setup'),
    Transition(label='Live Monitoring'),
    Transition(label='Variable Adjust'),
    Transition(label='Incident Injection'),
    Transition(label='Response Tracking'),
    Transition(label='Interlock Check'),
    Transition(label='Real-time Feedback'),
    Transition(label='Debrief Session'),
    Transition(label='Outcome Analysis'),
    Transition(label='Report Generation'),
    Transition(label='Improvement Plan')
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