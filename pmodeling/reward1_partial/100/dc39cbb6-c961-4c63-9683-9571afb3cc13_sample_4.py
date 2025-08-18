root = StrictPartialOrder(nodes=[
    Transition(label='Client Inquiry'),
    Transition(label='Requirement Gather'),
    Transition(label='Concept Sketch'),
    Transition(label='Client Feedback'),
    Transition(label='Revision Cycle'),
    Transition(label='Final Approval'),
    Transition(label='Art Creation'),
    Transition(label='Progress Update'),
    Transition(label='Quality Check'),
    Transition(label='Final Adjust'),
    Transition(label='Invoice Issue'),
    Transition(label='Shipment Prep'),
    Transition(label='Delivery Confirm'),
    Transition(label='Post Support'),
    Transition(label='License Setup'),
    Transition(label='Frame Arrange')
])

# Define the partial order edges
root.order.add_edge('Client Inquiry', 'Requirement Gather')
root.order.add_edge('Requirement Gather', 'Concept Sketch')
root.order.add_edge('Concept Sketch', 'Client Feedback')
root.order.add_edge('Client Feedback', 'Revision Cycle')
root.order.add_edge('Revision Cycle', 'Final Approval')
root.order.add_edge('Final Approval', 'Art Creation')
root.order.add_edge('Art Creation', 'Progress Update')
root.order.add_edge('Progress Update', 'Quality Check')
root.order.add_edge('Quality Check', 'Final Adjust')
root.order.add_edge('Final Adjust', 'Invoice Issue')
root.order.add_edge('Invoice Issue', 'Shipment Prep')
root.order.add_edge('Shipment Prep', 'Delivery Confirm')
root.order.add_edge('Delivery Confirm', 'Post Support')
root.order.add_edge('Post Support', 'License Setup')
root.order.add_edge('License Setup', 'Frame Arrange')