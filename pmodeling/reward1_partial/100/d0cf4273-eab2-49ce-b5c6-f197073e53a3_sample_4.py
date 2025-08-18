root = StrictPartialOrder(nodes=[
    Transition(label='Material Sourcing'),
    Transition(label='Cultural Verify'),
    Transition(label='Eco Transport'),
    Transition(label='Batch Storytelling'),
    Transition(label='Craftsman Assignment'),
    Transition(label='Product Creation'),
    Transition(label='Provenance Catalog'),
    Transition(label='Community Marketing'),
    Transition(label='Collector Targeting'),
    Transition(label='Package Assembly'),
    Transition(label='Local Cooperatives'),
    Transition(label='Environmental Audit'),
    Transition(label='Ethical Logistics'),
    Transition(label='Global Shipping'),
    Transition(label='Feedback Collection')
])

# Define the relationships between activities
root.order.add_edge(Transition(label='Material Sourcing'), Transition(label='Cultural Verify'))
root.order.add_edge(Transition(label='Cultural Verify'), Transition(label='Eco Transport'))
root.order.add_edge(Transition(label='Eco Transport'), Transition(label='Batch Storytelling'))
root.order.add_edge(Transition(label='Batch Storytelling'), Transition(label='Craftsman Assignment'))
root.order.add_edge(Transition(label='Craftsman Assignment'), Transition(label='Product Creation'))
root.order.add_edge(Transition(label='Product Creation'), Transition(label='Provenance Catalog'))
root.order.add_edge(Transition(label='Provenance Catalog'), Transition(label='Community Marketing'))
root.order.add_edge(Transition(label='Community Marketing'), Transition(label='Collector Targeting'))
root.order.add_edge(Transition(label='Collector Targeting'), Transition(label='Package Assembly'))
root.order.add_edge(Transition(label='Package Assembly'), Transition(label='Local Cooperatives'))
root.order.add_edge(Transition(label='Local Cooperatives'), Transition(label='Environmental Audit'))
root.order.add_edge(Transition(label='Environmental Audit'), Transition(label='Ethical Logistics'))
root.order.add_edge(Transition(label='Ethical Logistics'), Transition(label='Global Shipping'))
root.order.add_edge(Transition(label='Global Shipping'), Transition(label='Feedback Collection'))