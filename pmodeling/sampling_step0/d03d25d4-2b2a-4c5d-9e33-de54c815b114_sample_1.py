root = StrictPartialOrder(nodes=[
    Transition(label='Farm Registration'),
    Transition(label='Lot Tagging'),
    Transition(label='Soil Testing'),
    Transition(label='Harvest Logging'),
    Transition(label='Coffee Sorting'),
    Transition(label='Sensory Profiling'),
    Transition(label='Quality Scoring'),
    Transition(label='Blockchain Entry'),
    Transition(label='Environmental Audit'),
    Transition(label='Farmer Feedback'),
    Transition(label='Dynamic Pricing'),
    Transition(label='Roast Scheduling'),
    Transition(label='Batch Testing'),
    Transition(label='Certification Review'),
    Transition(label='Distribution Prep'),
    Transition(label='Consumer Feedback')
])

# Define the partial order structure
root.order.add_edge(Transition(label='Farm Registration'), Transition(label='Lot Tagging'))
root.order.add_edge(Transition(label='Lot Tagging'), Transition(label='Soil Testing'))
root.order.add_edge(Transition(label='Soil Testing'), Transition(label='Harvest Logging'))
root.order.add_edge(Transition(label='Harvest Logging'), Transition(label='Coffee Sorting'))
root.order.add_edge(Transition(label='Coffee Sorting'), Transition(label='Sensory Profiling'))
root.order.add_edge(Transition(label='Sensory Profiling'), Transition(label='Quality Scoring'))
root.order.add_edge(Transition(label='Quality Scoring'), Transition(label='Blockchain Entry'))
root.order.add_edge(Transition(label='Blockchain Entry'), Transition(label='Environmental Audit'))
root.order.add_edge(Transition(label='Environmental Audit'), Transition(label='Farmer Feedback'))
root.order.add_edge(Transition(label='Farmer Feedback'), Transition(label='Dynamic Pricing'))
root.order.add_edge(Transition(label='Dynamic Pricing'), Transition(label='Roast Scheduling'))
root.order.add_edge(Transition(label='Roast Scheduling'), Transition(label='Batch Testing'))
root.order.add_edge(Transition(label='Batch Testing'), Transition(label='Certification Review'))
root.order.add_edge(Transition(label='Certification Review'), Transition(label='Distribution Prep'))
root.order.add_edge(Transition(label='Distribution Prep'), Transition(label='Consumer Feedback'))