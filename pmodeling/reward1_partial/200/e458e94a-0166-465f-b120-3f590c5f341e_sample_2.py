root = StrictPartialOrder(nodes=[
    Transition(label='Inquiry Review'),
    Transition(label='Client Onboard'),
    Transition(label='Concept Draft'),
    Transition(label='Feedback Cycle'),
    Transition(label='Contract Setup'),
    Transition(label='Payment Schedule'),
    Transition(label='Material Sourcing'),
    Transition(label='Artwork Create'),
    Transition(label='Quality Check'),
    Transition(label='Frame Selection'),
    Transition(label='Packaging Prep'),
    Transition(label='Shipment Arrange'),
    Transition(label='Delivery Confirm'),
    Transition(label='Post-Sale Support'),
    Transition(label='Revision Manage'),
    Transition(label='Delay Mitigate')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Inquiry Review'), Transition(label='Client Onboard'))
root.order.add_edge(Transition(label='Client Onboard'), Transition(label='Concept Draft'))
root.order.add_edge(Transition(label='Concept Draft'), Transition(label='Feedback Cycle'))
root.order.add_edge(Transition(label='Feedback Cycle'), Transition(label='Contract Setup'))
root.order.add_edge(Transition(label='Contract Setup'), Transition(label='Payment Schedule'))
root.order.add_edge(Transition(label='Payment Schedule'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Artwork Create'))
root.order.add_edge(Transition(label='Artwork Create'), Transition(label='Quality Check'))
root.order.add_edge(Transition(label='Quality Check'), Transition(label='Frame Selection'))
root.order.add_edge(Transition(label='Frame Selection'), Transition(label='Packaging Prep'))
root.order.add_edge(Transition(label='Packaging Prep'), Transition(label='Shipment Arrange'))
root.order.add_edge(Transition(label='Shipment Arrange'), Transition(label='Delivery Confirm'))
root.order.add_edge(Transition(label='Delivery Confirm'), Transition(label='Post-Sale Support'))
root.order.add_edge(Transition(label='Post-Sale Support'), Transition(label='Revision Manage'))
root.order.add_edge(Transition(label='Revision Manage'), Transition(label='Delay Mitigate'))