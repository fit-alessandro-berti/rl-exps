root = StrictPartialOrder(nodes=[
    Transition(label='Farm Selection'),
    Transition(label='Sample Testing'),
    Transition(label='Trade Negotiation'),
    Transition(label='Micro-Lot Sorting'),
    Transition(label='Fermentation Control'),
    Transition(label='Sensory Profiling'),
    Transition(label='Roast Calibration'),
    Transition(label='Blend Creation'),
    Transition(label='Sustainability Audit'),
    Transition(label='Packaging Design'),
    Transition(label='Quality Inspection'),
    Transition(label='Inventory Sync'),
    Transition(label='Logistics Planning'),
    Transition(label='Cafe Training'),
    Transition(label='Dynamic Pricing'),
    Transition(label='Customer Feedback'),
    Transition(label='Traceability Logging')
])

root.order.add_edge(Transition(label='Farm Selection'), Transition(label='Sample Testing'))
root.order.add_edge(Transition(label='Sample Testing'), Transition(label='Trade Negotiation'))
root.order.add_edge(Transition(label='Trade Negotiation'), Transition(label='Micro-Lot Sorting'))
root.order.add_edge(Transition(label='Micro-Lot Sorting'), Transition(label='Fermentation Control'))
root.order.add_edge(Transition(label='Fermentation Control'), Transition(label='Sensory Profiling'))
root.order.add_edge(Transition(label='Sensory Profiling'), Transition(label='Roast Calibration'))
root.order.add_edge(Transition(label='Roast Calibration'), Transition(label='Blend Creation'))
root.order.add_edge(Transition(label='Blend Creation'), Transition(label='Sustainability Audit'))
root.order.add_edge(Transition(label='Sustainability Audit'), Transition(label='Packaging Design'))
root.order.add_edge(Transition(label='Packaging Design'), Transition(label='Quality Inspection'))
root.order.add_edge(Transition(label='Quality Inspection'), Transition(label='Inventory Sync'))
root.order.add_edge(Transition(label='Inventory Sync'), Transition(label='Logistics Planning'))
root.order.add_edge(Transition(label='Logistics Planning'), Transition(label='Cafe Training'))
root.order.add_edge(Transition(label='Cafe Training'), Transition(label='Dynamic Pricing'))
root.order.add_edge(Transition(label='Dynamic Pricing'), Transition(label='Customer Feedback'))
root.order.add_edge(Transition(label='Customer Feedback'), Transition(label='Traceability Logging'))