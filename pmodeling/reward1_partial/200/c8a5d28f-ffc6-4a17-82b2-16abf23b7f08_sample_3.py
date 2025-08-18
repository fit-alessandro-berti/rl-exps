root = StrictPartialOrder(nodes=[
    Transition(label='Milk Sourcing'),
    Transition(label='Quality Testing'),
    Transition(label='Milk Pasteurize'),
    Transition(label='Culture Addition'),
    Transition(label='Curd Cutting'),
    Transition(label='Whey Drain'),
    Transition(label='Cheese Molding'),
    Transition(label='Controlled Aging'),
    Transition(label='Sensory Check'),
    Transition(label='Health Certify'),
    Transition(label='Custom Labeling'),
    Transition(label='Cold Packaging'),
    Transition(label='Logistics Setup'),
    Transition(label='Export Docs'),
    Transition(label='Customs Clearance'),
    Transition(label='Shipment Track'),
    Transition(label='Client Feedback')
])

root.order.add_edge(Transition(label='Milk Sourcing'), Transition(label='Quality Testing'))
root.order.add_edge(Transition(label='Quality Testing'), Transition(label='Milk Pasteurize'))
root.order.add_edge(Transition(label='Milk Pasteurize'), Transition(label='Culture Addition'))
root.order.add_edge(Transition(label='Culture Addition'), Transition(label='Curd Cutting'))
root.order.add_edge(Transition(label='Curd Cutting'), Transition(label='Whey Drain'))
root.order.add_edge(Transition(label='Whey Drain'), Transition(label='Cheese Molding'))
root.order.add_edge(Transition(label='Cheese Molding'), Transition(label='Controlled Aging'))
root.order.add_edge(Transition(label='Controlled Aging'), Transition(label='Sensory Check'))
root.order.add_edge(Transition(label='Sensory Check'), Transition(label='Health Certify'))
root.order.add_edge(Transition(label='Health Certify'), Transition(label='Custom Labeling'))
root.order.add_edge(Transition(label='Custom Labeling'), Transition(label='Cold Packaging'))
root.order.add_edge(Transition(label='Cold Packaging'), Transition(label='Logistics Setup'))
root.order.add_edge(Transition(label='Logistics Setup'), Transition(label='Export Docs'))
root.order.add_edge(Transition(label='Export Docs'), Transition(label='Customs Clearance'))
root.order.add_edge(Transition(label='Customs Clearance'), Transition(label='Shipment Track'))
root.order.add_edge(Transition(label='Shipment Track'), Transition(label='Client Feedback'))