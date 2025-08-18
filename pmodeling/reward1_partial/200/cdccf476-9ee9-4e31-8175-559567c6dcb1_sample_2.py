root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Curd Formation'),
    Transition(label='Microbial Test'),
    Transition(label='Whey Removal'),
    Transition(label='Pressing Cheese'),
    Transition(label='Salt Application'),
    Transition(label='Aging Control'),
    Transition(label='Quality Check'),
    Transition(label='Eco Packaging'),
    Transition(label='Inventory Log'),
    Transition(label='Temp Monitoring'),
    Transition(label='Carrier Booking'),
    Transition(label='Trace Recording'),
    Transition(label='Feedback Review'),
    Transition(label='Compliance Audit'),
    Transition(label='Batch Adjustment')
])

root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Curd Formation'))
root.order.add_edge(Transition(label='Curd Formation'), Transition(label='Microbial Test'))
root.order.add_edge(Transition(label='Microbial Test'), Transition(label='Whey Removal'))
root.order.add_edge(Transition(label='Whey Removal'), Transition(label='Pressing Cheese'))
root.order.add_edge(Transition(label='Pressing Cheese'), Transition(label='Salt Application'))
root.order.add_edge(Transition(label='Salt Application'), Transition(label='Aging Control'))
root.order.add_edge(Transition(label='Aging Control'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Eco Packaging'))
root.order.add_edge(Transition(label='Eco Packaging'), Transition(label='Inventory Log'))
root.order.add_edge(Transition(label='Inventory Log'), Transition(label='Temp Monitoring'))
root.order.add_edge(Transition(label='Temp Monitoring'), Transition(label='Carrier Booking'))
root.order.add_edge(Transition(label='Carrier Booking'), Transition(label='Trace Recording'))
root.order.add_edge(Transition(label='Trace Recording'), Transition(label='Feedback Review'))
root.order.add_edge(Transition(label='Feedback Review'), Transition(label='Compliance Audit'))
root.order.add_edge(Transition(label='Compliance Audit'), Transition(label='Batch Adjustment'))