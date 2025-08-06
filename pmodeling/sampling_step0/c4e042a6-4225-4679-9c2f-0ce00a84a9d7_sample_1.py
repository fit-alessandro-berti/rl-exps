root = StrictPartialOrder(nodes=[
    Transition(label='Material Sourcing'),
    Transition(label='Supplier Audit'),
    Transition(label='Credential Verify'),
    Transition(label='Design Concept'),
    Transition(label='Prototype Build'),
    Transition(label='Quality Review'),
    Transition(label='Artisan Assign'),
    Transition(label='Batch Scheduling'),
    Transition(label='Custom Approvals'),
    Transition(label='Inventory Adjust'),
    Transition(label='Production Sync'),
    Transition(label='Shipping Plan'),
    Transition(label='Compliance Check'),
    Transition(label='Feedback Loop'),
    Transition(label='Market Target'),
    Transition(label='Order Fulfill'),
    Transition(label='Sustainability'),
    Transition(label='Customer Engage')
])

root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Supplier Audit'))
root.order.add_edge(Transition(label='Supplier Audit'), Transition(label='Credential Verify'))
root.order.add_edge(Transition(label='Credential Verify'), Transition(label='Design Concept'))
root.order.add_edge(Transition(label='Design Concept'), Transition(label='Prototype Build'))
root.order.add_edge(Transition(label='Prototype Build'), Transition(label='Quality Review'))
root.order.add_edge(Transition(label='Quality Review'), Transition(label='Artisan Assign'))
root.order.add_edge(Transition(label='Artisan Assign'), Transition(label='Batch Scheduling'))
root.order.add_edge(Transition(label='Batch Scheduling'), Transition(label='Custom Approvals'))
root.order.add_edge(Transition(label='Custom Approvals'), Transition(label='Inventory Adjust'))
root.order.add_edge(Transition(label='Inventory Adjust'), Transition(label='Production Sync'))
root.order.add_edge(Transition(label='Production Sync'), Transition(label='Shipping Plan'))
root.order.add_edge(Transition(label='Shipping Plan'), Transition(label='Compliance Check'))
root.order.add_edge(Transition(label='Compliance Check'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Market Target'))
root.order.add_edge(Transition(label='Market Target'), Transition(label='Order Fulfill'))
root.order.add_edge(Transition(label='Order Fulfill'), Transition(label='Sustainability'))
root.order.add_edge(Transition(label='Sustainability'), Transition(label='Customer Engage'))