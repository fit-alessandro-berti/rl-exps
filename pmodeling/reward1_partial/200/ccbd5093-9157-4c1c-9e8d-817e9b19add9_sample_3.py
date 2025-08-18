root = StrictPartialOrder(nodes=[
    Transition(label='Scan Markets'),
    Transition(label='Host Workshops'),
    Transition(label='Form Teams'),
    Transition(label='Develop Prototypes'),
    Transition(label='Simulate Tests'),
    Transition(label='Collect Feedback'),
    Transition(label='Review Ethics'),
    Transition(label='Conduct Analysis'),
    Transition(label='Identify Partners'),
    Transition(label='Align Strategy'),
    Transition(label='Launch Pilots'),
    Transition(label='Monitor Trends'),
    Transition(label='AI Analytics'),
    Transition(label='Pivot Plans'),
    Transition(label='Cycle Renewal')
])

root.order.add_edge(Transition(label='Scan Markets'), Transition(label='Host Workshops'))
root.order.add_edge(Transition(label='Host Workshops'), Transition(label='Form Teams'))
root.order.add_edge(Transition(label='Form Teams'), Transition(label='Develop Prototypes'))
root.order.add_edge(Transition(label='Develop Prototypes'), Transition(label='Simulate Tests'))
root.order.add_edge(Transition(label='Simulate Tests'), Transition(label='Collect Feedback'))
root.order.add_edge(Transition(label='Collect Feedback'), Transition(label='Review Ethics'))
root.order.add_edge(Transition(label='Review Ethics'), Transition(label='Conduct Analysis'))
root.order.add_edge(Transition(label='Conduct Analysis'), Transition(label='Identify Partners'))
root.order.add_edge(Transition(label='Identify Partners'), Transition(label='Align Strategy'))
root.order.add_edge(Transition(label='Align Strategy'), Transition(label='Launch Pilots'))
root.order.add_edge(Transition(label='Launch Pilots'), Transition(label='Monitor Trends'))
root.order.add_edge(Transition(label='Monitor Trends'), Transition(label='AI Analytics'))
root.order.add_edge(Transition(label='AI Analytics'), Transition(label='Pivot Plans'))
root.order.add_edge(Transition(label='Pivot Plans'), Transition(label='Cycle Renewal'))