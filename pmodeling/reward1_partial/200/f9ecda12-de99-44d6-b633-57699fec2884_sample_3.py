root = StrictPartialOrder(nodes=[
    Transition(label='Concept Approve'),
    Transition(label='Budget Align'),
    Transition(label='Design Review'),
    Transition(label='Structure Simulate'),
    Transition(label='Material Procure'),
    Transition(label='Vendor Select'),
    Transition(label='Permit Apply'),
    Transition(label='Safety Check'),
    Transition(label='Site Prep'),
    Transition(label='Logistics Plan'),
    Transition(label='Fabricate Parts'),
    Transition(label='Assemble Onsite'),
    Transition(label='Quality Inspect'),
    Transition(label='Weather Monitor'),
    Transition(label='Public Unveil'),
    Transition(label='Maintenance Plan'),
    Transition(label='Stakeholder Meet')
])

root.order.add_edge(Transition(label='Concept Approve'), Transition(label='Budget Align'))
root.order.add_edge(Transition(label='Budget Align'), Transition(label='Design Review'))
root.order.add_edge(Transition(label='Design Review'), Transition(label='Structure Simulate'))
root.order.add_edge(Transition(label='Structure Simulate'), Transition(label='Material Procure'))
root.order.add_edge(Transition(label='Material Procure'), Transition(label='Vendor Select'))
root.order.add_edge(Transition(label='Vendor Select'), Transition(label='Permit Apply'))
root.order.add_edge(Transition(label='Permit Apply'), Transition(label='Safety Check'))
root.order.add_edge(Transition(label='Safety Check'), Transition(label='Site Prep'))
root.order.add_edge(Transition(label='Site Prep'), Transition(label='Logistics Plan'))
root.order.add_edge(Transition(label='Logistics Plan'), Transition(label='Fabricate Parts'))
root.order.add_edge(Transition(label='Fabricate Parts'), Transition(label='Assemble Onsite'))
root.order.add_edge(Transition(label='Assemble Onsite'), Transition(label='Quality Inspect'))
root.order.add_edge(Transition(label='Quality Inspect'), Transition(label='Weather Monitor'))
root.order.add_edge(Transition(label='Weather Monitor'), Transition(label='Public Unveil'))
root.order.add_edge(Transition(label='Public Unveil'), Transition(label='Maintenance Plan'))
root.order.add_edge(Transition(label='Maintenance Plan'), Transition(label='Stakeholder Meet'))