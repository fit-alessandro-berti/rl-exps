root = StrictPartialOrder(nodes=[
    Transition(label='Permit Securing'),
    Transition(label='Structure Check'),
    Transition(label='Soil Testing'),
    Transition(label='Water Analysis'),
    Transition(label='Material Sourcing'),
    Transition(label='Planter Setup'),
    Transition(label='Sensor Install'),
    Transition(label='Irrigation Setup'),
    Transition(label='Vendor Liaison'),
    Transition(label='Staff Training'),
    Transition(label='Pest Control'),
    Transition(label='Produce Marketing'),
    Transition(label='Crop Rotation'),
    Transition(label='Health Audit'),
    Transition(label='Waste Composting')
])
root.order.add_edge(Transition(label='Permit Securing'), Transition(label='Structure Check'))
root.order.add_edge(Transition(label='Structure Check'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='Water Analysis'))
root.order.add_edge(Transition(label='Water Analysis'), Transition(label='Material Sourcing'))
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Planter Setup'))
root.order.add_edge(Transition(label='Planter Setup'), Transition(label='Sensor Install'))
root.order.add_edge(Transition(label='Sensor Install'), Transition(label='Irrigation Setup'))
root.order.add_edge(Transition(label='Irrigation Setup'), Transition(label='Vendor Liaison'))
root.order.add_edge(Transition(label='Vendor Liaison'), Transition(label='Staff Training'))
root.order.add_edge(Transition(label='Staff Training'), Transition(label='Pest Control'))
root.order.add_edge(Transition(label='Pest Control'), Transition(label='Produce Marketing'))
root.order.add_edge(Transition(label='Produce Marketing'), Transition(label='Crop Rotation'))
root.order.add_edge(Transition(label='Crop Rotation'), Transition(label='Health Audit'))
root.order.add_edge(Transition(label='Health Audit'), Transition(label='Waste Composting'))